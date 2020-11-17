# Copyright © 2019-2020 Alexander L. Hayes
# MIT License

# Rules for automated testing, code style, and linting.
test:
	pytest --cov=abb abb
style:
	black abb/
	pycodestyle --max-line-length=100 abb/
