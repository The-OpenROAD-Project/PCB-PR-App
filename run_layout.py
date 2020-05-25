"""
Run PCB Layout Job.

Usage:
    run_layout.py [options] KICAD_PCB

Options:
    --skip_placement  Don't run autoplacement.
    -p PITER          Placement iterations [default: 1000].
    -m MOVES          Moves per placement iteration [default: 25].
    -r RITERS         Ripup and reroute iterations [default: 2].
    -e ENLARGE        Enlarge board boundary for routing [default: 0].
    -l CHANGEW        Layer change weight for routing [default: 1000].

"""

from docopt import docopt

from ucsdpcb import PcbPlacer
from ucsdpcb import PcbRouter
from ucsdpcb import PcbDB


def main(arguments):
    print(arguments)
    
    print('Loading database...')
    db = PcbDB.kicadPcbDataBase(arguments['KICAD_PCB'])
    db.printNodes()
    db.removeRoutedSegmentsAndVias()

    if not arguments['--skip_placement']:
        placer = PcbPlacer.GridBasedPlacer(db)
        placer.set_num_iterations(arguments['-p'])
        placer.set_iterations_moves(arguments['-m'])
        placer.set_two_sided(True)
        placer.set_rtree(False)

        print('Placing...')
        placer.test_placer_flow()
        db.printKiCad()

    router = PcbRouter.GridBasedRouter(db)
    router.initialization()
    router.set_num_iterations(arguments['-r'])
    router.set_enlarge_boundary(arguments['-e'])
    router.set_layer_change_weight(arguments['-l'])
    
    print('Routing...')
    router.route()
    db.printKiCad()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')
    arguments['-p'] = int(arguments['-p'])
    arguments['-m'] = int(arguments['-m'])
    arguments['-r'] = int(arguments['-r'])
    arguments['-e'] = int(arguments['-e'])
    arguments['-l'] = int(arguments['-l'])
    main(arguments)


