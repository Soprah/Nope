THIS_DIR = /home/peter/Softwareprojekt/Github4/Nope


.PHONY = run_server
run_server:
	@export PYTHONPATH=${PYTHONPATH}:${THIS_DIR} ; \
    python3  ${THIS_DIR}/src/network/Events.py