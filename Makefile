THIS_DIR = /home/peter/Softwareprojekt/GitHub2/Nope

.PHONY = run_client
run_client:
	@export PYTHONPATH=${PYTHONPATH}:${THIS_DIR} ; \
    python  ${THIS_DIR}/src/network/client.py