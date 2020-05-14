#set -e

echo "Running tests .."
echo "================"

echo "run_layout.py test"
python3 run_layout.py tests/placement_test_full_mix.kicad_pcb
echo "Success"

