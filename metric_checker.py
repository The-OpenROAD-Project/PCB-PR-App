#!/usr/bin/env python3
"""
metric_checker.py.

The main purpose of this script is to extract metrics from PCB layouts in
the kicad_pcb format.

Usage:
    metric_checker.py <kicad_pcb_file>

"""

import math

from docopt import docopt


class Location(object):
    def __init__(self, x=None, y=None):
        if x is None:
            x = 0.0
        self.x = x

        if y is None:
            y = 0.0
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Pad(object):
    def __init__(self, component, index, x, y, net):
        # print('new pad:', x, y)
        self.location = Location(x, y)
        self.net = net
        self.component = component
        self.index = index

    def distance(self, other):
        return self.location.distance(other.location)

    def pp_name(self):
        return '(pad ' + self.component.index + ' ' + self.index + ')'

    def rotate90(self):
        x = self.location.x
        y = self.location.y
        self.location.x = y
        self.location.y = -x

    def absolution_location(self):
        return Location(self.location.x+self.component.location.x, self.location.y+self.component.location.y)

class Box(object):
    def __init__(self):
        self.x_max = 0.0
        self.x_min = 0.0
        self.y_max = 0.0
        self.y_min = 0.0

    def check_overlap_1d(self, a_max, a_min, b_max, b_min):
        if a_max < b_max:
            return self.check_overlap_1d(b_max, b_min, a_max, a_min)
        # no overlap
        if b_max < a_min:
            return 0
        union_size = a_max - b_min
        top_loss = abs(a_max - b_max)
        bottom_loss = abs(a_min - b_min)
        overlap = union_size - top_loss - bottom_loss
        return max(overlap, 0)

    def check_overlap(self, other, self_o, other_o):
        w = self.check_overlap_1d(
            self.x_max + self_o.x, 
            self.x_min + self_o.x, 
            other.x_max + other_o.x, 
            other.x_min + other_o.x
        )
        if w == 0:
            return 0
        h = self.check_overlap_1d(
            self.y_max + self_o.y, 
            self.y_min + self_o.y, 
            other.y_max + other_o.y, 
            other.y_min + other_o.y
        )
        if h == 0:
            return 0

        # print('Checking overlap')
        # print('w:', w)
        # print('h:', h)

        return w * h

    def rotate90(self):
        x_max = self.x_max 
        x_min = self.x_min
        self.x_max = self.y_max
        self.x_min = self.y_min
        self.y_max = x_min
        self.y_min = x_max

        x_max = max(self.x_max, self.x_min)
        x_min = min(self.x_max, self.x_min)
        y_max = max(self.y_max, self.y_min)
        y_min = min(self.y_max, self.y_min)

        self.x_max = x_max
        self.x_min = x_min
        self.y_max = y_max
        self.y_min = y_min


class Module(object):
    def __init__(self, index=None, x=None, y=None, r=None):
        self.pads = {}
        self.index = index
        self.location = Location(x, y)
        if r is None:
            r = 0.0
        self.rotation = r
        self.top_box = Box()
        self.bottom_box = Box()
        self.old_location = Location(x, y)

    def save_location(self):
        self.old_location.x = self.location.x
        self.old_location.y = self.location.y

    def reset_location(self):
        self.location.x = self.old_location.x
        self.location.y = self.old_location.y

    def check_overlap(self, other):
        top = self.top_box.check_overlap(other.top_box, self.location, other.location)
        bottom = self.bottom_box.check_overlap(other.bottom_box, self.location, other.location)
        return top + bottom

    def add_pad(self, index, node):
        self.pads[index] = node

    def rotate90(self):
        self.top_box.rotate90()
        self.bottom_box.rotate90()

        for index in self.pads:
            pad = self.pads[index]
            x = pad.location.x
            y = pad.location.y
            pad.location.x = y
            pad.location.y = -x
            # print('rotating pad:', x, '>', pad.location.x, y, '>', pad.location.y )

    def move_to(self, x, y):
        self.location.x = x
        self.location.y = y

    def move_by(self, x, y):
        self.location.x = self.location.x + x
        self.location.y = self.location.y + y

    def from_node(self, node):
        self.index = node.word(1)

        ## Location
        ats = [n for n in node.children if n.keyword() == 'at']
        assert len(ats) == 1
        at = ats[0]
        assert (len(at.words()) == 3) or (len(at.words()) == 4), len(at.children)
        self.location = Location(float(at.word(1)), float(at.word(2)))
        if len(at.words()) == 4:
            self.r = float(at.word(-1))
        else:
            self.r = 0.0
        while self.r < 0:
            self.r += 360
        assert self.r in [0, 90, 180, 270], self.r

        ## Courtyard
        polys = [n for n in node.children if n.keyword() == 'fp_poly']
        assert len(polys) == 1
        for p in polys:
            layer = [n for n in p.children if n.keyword() == 'layer'][0]
            if layer.word(-1) == 'F.CrtYd':
                top = True
            else:
                assert layer.word(-1) == 'B.CrtYd'
                top = False

            pts = [n for n in p.children if n.keyword() == 'pts']
            assert len(pts) == 1
            pts = pts[0]
            xys = [n for n in pts.children if n.keyword() == 'xy']
            for xy in xys:
                x = float(xy.word(1))
                y = float(xy.word(2))
                if top:
                    box = self.top_box
                else:
                    box = self.bottom_box
                box.x_max = max(box.x_max, x)
                box.x_min = min(box.x_min, x)
                box.y_max = max(box.y_max, y)
                box.y_min = min(box.y_min, y)
            
        # print('Top bound:', self.top_box.x_max, self.top_box.x_min, self.top_box.y_max, self.top_box.y_min)
        # print('Bottom bound:', self.bottom_box.x_max, self.bottom_box.x_min, self.bottom_box.y_max, self.bottom_box.y_min)

        ## Pads
        for p in [p for p in node.children if p.keyword() == 'pad']:
            index = p.word(1)
            ats = [n for n in p.children if n.keyword() == 'at']
            assert len(ats) == 1
            at = ats[0]

            nets = [n for n in p.children if n.keyword() == 'net']
            assert len(nets) == 1 or len(nets) == 0
            if len(nets) == 1:
                net = nets[0]
                net_name = net.word(-1)
                net_index = int(net.word(1))
            else:
                net_name = None
                net_index = None

            self.pads[index] = Pad(component=self, index=index, x=float(at.word(1)), y=float(at.word(2)), net=net_name)

        # print('Rotating:', self.r)
        if self.r == 90:
            self.rotate90()
        elif self.r == 180:
            self.rotate90()
            self.rotate90()
        elif self.r == 270:
            self.rotate90()
            self.rotate90()
            self.rotate90()


class Node(object):
    """
    S-expression node class. Has parents, children, and text. Doesn't handle quoted escapes yet but it should in the future.
    """
    def __init__(self, text='', parent=None, children=None, t_start=0, t_end=0):
        self.text = text
        self.t_start = t_start
        self.t_end = t_end
        self.parent = parent
        if self.parent is not None:
            self.parent.children.append(self)

        if children is None:
            self.children = []

    def add_c(self, c):
        self.text += c
        if self.parent is not None:
            
            self.parent.add_c(c)

    def keyword(self):
        if len(self.text) > 0:
            return self.text.split()[0].strip('()')
        else:
            return ''

    def word(self, i):
        return self.text.strip().strip('()').split()[i].strip('()')

    def words(self):
        return [i.strip('()').strip() for i in self.text.strip().strip('()').split()]


def get_keywords(text):
    # find keywords
    splits = text.split('(')
    splits = [s.split() for s in splits]
    keywords = set()
    for s in splits:
        if len(s) > 0:
            keywords.add(s[0])

    keywords = list(keywords)
    keywords.sort()
    return keywords


def calculate_overlap(modules_dict):
    module_list = list(modules_dict.values())
    total_overlap = 0.0
    for i, m in enumerate(module_list):
        for j, n in enumerate(module_list[i:]):
            if m == n:
                continue
            overlap = m.check_overlap(n)
            # if overlap > 0:
                # print(m.index, n.index, overlap)
            total_overlap += overlap
    return total_overlap


def calculate_wirelength(nets_to_pads):
    hpwl = 0.0
    for net, pads in nets_to_pads.items():
        if net is None:
            continue
        max_x = -9e99
        min_x = 9e99
        max_y = -9e99
        min_y = 9e99

        # print(net)

        for pad in pads:
            max_x = max(max_x, pad.location.x+pad.component.location.x)
            min_x = min(min_x, pad.location.x+pad.component.location.x)
            max_y = max(max_y, pad.location.y+pad.component.location.y)
            min_y = min(min_y, pad.location.y+pad.component.location.y)
            # print(
            #     'pad.location.x:', pad.location.x+pad.component.location.x,
            #     'pad.location.y:', pad.location.y+pad.component.location.y
            # )

            # print('max_x:', max_x, 'min_x:', min_x, 'max_y:', max_y, 'min_y:', min_y)
        hpwl += max_x - min_x
        hpwl += max_y - min_y
    return hpwl


def main(arguments):
    # print(arguments)
    print('Checking metrics for: ' + str(arguments['<kicad_pcb_file>']))
    
    with open(arguments['<kicad_pcb_file>'], 'r') as f:
        text = f.read()


    text = text.replace('( ', '(')
    text = text.replace(' )', ')')

    node_stack = []
    nodes = []
    for i, c in enumerate(text):
        if c == '(':
            # print(str(len(nodes)), 'New node:', text[i:i+15].strip())
            if len(node_stack) > 0:
                node_stack.append(Node(parent=node_stack[-1]))
            else:
                node_stack.append(Node())
            node_stack[-1].t_start = i
            nodes.append(node_stack[-1])
        elif c == ')':
            node_stack[-1].t_end = i+1
            node_stack.pop()

    node_types = {}
    for n in nodes:
        n.text = text[n.t_start:n.t_end]
        try:
            node_types[n.keyword()].append(n)
        except KeyError:
            node_types[n.keyword()] = [n]


    # print('Found node types: ' + str(node_types.keys()))

    # routed length
    segments = []
    total_length = 0.0
    for n in node_types['segment']:
        start = [s for s in n.children if s.keyword() == 'start']
        assert len(start) == 1
        start = start[0]
        (sx, sy) = (float(start.word(1)), float(start.word(2)))
        end = [s for s in n.children if s.keyword() == 'end']
        assert len(end) == 1
        end = end[0]
        (ex, ey) = (float(end.word(1)), float(end.word(2)))
        # print(start.text, end.text)
        # print((sx, sy), (ex, ey))
        total_length += math.sqrt( ((sx - ex)**2) + ((sy - ey)**2) )
    print('\tTotal routed length: ' + str(total_length))

    # via counts
    vias = []
    micro_vias = []
    for n in node_types['via']:
        if n.word(1) == 'micro':
            micro_vias.append(n)
        else:
            vias.append(n)

    print('\tTH via count: ' + str(len(vias)))
    print('\tLaser via count: ' + str(len(micro_vias)))


    # for n in node_types

    # # overlap
    # modules = {}
    # for n in node_types['module']:
    #     module_name = n.word(1)
    #     modules[module_name] = Module()
    #     modules[module_name].from_node(n)

    # # print('Got', len(modules), 'modules')

    # overlap = calculate_overlap(modules)
    # print('Total overlap:', overlap)

    # # nets
    # nets_to_pads = {}
    # for module in modules.values():
    #     for pad in module.pads.values():
    #         net = pad.net
    #         try:
    #             nets_to_pads[net].append(pad)
    #         except KeyError:
    #             nets_to_pads[net] = [pad]
    # print('Nets:')
    # for net, pads in nets_to_pads.items():
        # print('\t', net)
        # for p in [p.component.index + '.' + p.index for p in pads]:
            # print('\t\t', p)

    # wire_length = calculate_wirelength(nets_to_pads)
    # print('Total hpwl:', wire_length)


    # closest_pads = {}
    # for net, pads in nets_to_pads.items():
    #     if net is None:
    #         continue
    #     for pad in pads:
    #         for other_pad in pads:
    #             if pad == other_pad:
    #                 continue
    #             if pad.component == other_pad.component:
    #                 continue
    #             if other_pad in closest_pads:
    #                 continue
    #             if pad.component.index.startswith('R') and other_pad.component.index.startswith('R'):
    #                 continue
    #             if pad.component.index.startswith('C') and other_pad.component.index.startswith('C'):
    #                 continue
    #             if pad.component.index.startswith('R') and other_pad.component.index.startswith('C'):
    #                 continue
    #             if pad.component.index.startswith('C') and other_pad.component.index.startswith('R'):
    #                 continue

    #             distance = pad.distance(other_pad) * 1.1 + 1.0
    #             if pad not in closest_pads:
    #                 closest_pads[pad] = (other_pad, net, distance)
    #             else:
    #                 old_distance = closest_pads[pad][2]
    #                 if distance < old_distance:
    #                     closest_pads[pad] = (other_pad, net, distance)

    # constraint_file_name = arguments['<kicad_pcb_file>'] + '.constraints'
    # with open(constraint_file_name, 'w') as f:
    #     for pad, info in closest_pads.items():
    #         constraint_str = (
    #             '(distance_constraint ' +
    #             pad.pp_name() + ' ' + 
    #             info[0].pp_name() + ' ' + 
    #             '(max ' + round(str(info[2]), 3) + ') ' +
    #             '(net ' + info[1] + ')'
    #             + ')'
    #         )
    #         print(constraint_str)
    #         f.write(constraint_str + '\n')
    # print('Wrote', len(closest_pads), 'distance constraints')


    # import random
    # import time

    # scale = 1
    # for m in modules.values():
    #     m.save_location()

    # old_overlap = calculate_overlap(modules)
    # old_hpwl = calculate_wirelength(nets_to_pads)
    # while True:
    #     # time.sleep(0.5)
    #     # for m in modules.values():
    #     # with  as m:            
    #     random.choice(list(modules.values())).move_by(
    #         (random.random()-0.5)*scale*2, 
    #         (random.random()-0.5)*scale*2
    #     )
    #     new_overlap = calculate_overlap(modules)
    #     new_hpwl = calculate_wirelength(nets_to_pads)
    #     print(old_overlap+old_hpwl, new_overlap+new_hpwl, new_overlap, new_hpwl)
    #     if (new_overlap <= old_overlap) and (new_hpwl < old_hpwl):
    #         for m in modules.values():
    #             m.save_location()
    #         old_overlap = new_overlap
    #         old_hpwl = new_hpwl
    #     else:
    #         for m in modules.values():
    #             m.reset_location()






if __name__ == "__main__":
    arguments = docopt(__doc__, version='Metric Checker 0.1')
    main(arguments)



