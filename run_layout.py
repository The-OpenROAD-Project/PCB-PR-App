"""
Run PCB Layout Job.

This script is a template for using this place and route framework. This script
removes all routing in the kicad_pcb file given, then places and routes the
design.

Usage:
    run_layout.py [options] KICAD_PCB

Options:
    --skip_placement  Don't run autoplacement.
    -p PITER          Placement iterations [default: 4000].
    -m MOVES          Moves per placement iteration [default: 25].
    -r RITERS         Ripup and reroute iterations [default: 20].
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
    db.removeRoutedSegmentsAndVias() # start without any previous routing

    if not arguments['--skip_placement']:
        placer = PcbPlacer.GridBasedPlacer(db)
        placer.set_num_iterations(arguments['-p'])
        placer.set_iterations_moves(arguments['-m'])
        placer.set_rtree(True)
        placer.set_two_sided(False)
        placer.set_base_lam(0.1329209929630061)
        placer.set_lamtemp_update(0.8853585421875213)
        placer.set_lambda_schedule(0.9753893051539414)

        print('Placing...')
        placer.test_placer_flow()
        db.printKiCad()

    router = PcbRouter.GridBasedRouter(db)
    router.set_num_iterations(arguments['-r'])
    router.set_enlarge_boundary(arguments['-e'])
    router.set_layer_change_weight(arguments['-l'])
    
    print('Routing...')
    router.initialization() # must be the last call to router before route()
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


