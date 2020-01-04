from nltk import Tree
def postprocess_layer(t, cur_layer=""):
    if len(t) == 0 or isinstance(t, str):
        return

    # if current label is module, find the layer it's on
    if t.label() == "module":
        for c in t:
            if isinstance(c, str):
                continue
            elif c.label() == "layer":
                cur_layer = c[0]
    elif t.label == "pad": # if pad, set the layer to cur layer
        for c in t:
            if isinstance(c, str):
                continue
            elif c.label() == "layers":
                # iterate through layers and swap out layer type for the cur_layer
                for cc in c:
                    if cc == "Top" or cc == "Bottom":
                        cc.set_label(cur_layer)
    for c in t:
        postprocess_layer(c, cur_layer)

def check_output(fname):
    # read file into tree structure
    s = open(fname, 'r').read().replace('\n','')
    t = Tree.fromstring(s)

    postprocess_layer(t)

    # write tree to file
    with open('./'+fname+'_parsed_output','w') as f:
        f.write(str(t))
