collectstatic:
	./manage.py collectstatic --noinput
	@echo "-----"
	@echo

migratedb:
	./manage.py migrate
	@echo "-----"
	@echo

predeploy: collectstatic migratedb
