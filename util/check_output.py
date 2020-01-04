from nltk import Tree

def check_output(fname):  
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
        elif t.label() == "pad": # if pad, set the layer to cur layer
            for c in t:
                if isinstance(c, str):
                    continue
                elif c.label() == "layers":
                    # iterate through layers and swap out layer type for the cur_layer
                    for i,cc in enumerate(c):
                        if cc == "Top" or cc == "Bottom":
                            c[i] = cur_layer
        for c in t:
            postprocess_layer(c, cur_layer)

    # read file into tree structure
    print('reading ' + fname)
    s = open(fname, 'r').read()
    t = Tree.fromstring(s,leaf_pattern="\".*\"|[^\s]+")

    postprocess_layer(t)

    print('writing ' + './checked.'+fname)
    # write tree to file
    with open('./checked.'+fname,'w') as f:
        f.write(str(t))
