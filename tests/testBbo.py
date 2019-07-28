if __name__ == '__main__':
	from algorithms.normal.normal import normal
	from algorithms.bbo.bbo import bbo
	from benchmarks.time import MAX_IMMIGRATION, MAX_EMIGRATION, MAX_MUTATION

	Desc1 = """
		for this first part of the test, we fix AX_EMIGRATION, MAX_IMMIGRATION, MAX_MUTATION
		(see the time.py), and play on the iterations and population size.
	"""

	print(Desc1)

	for population in [50, 100, 150, 200]:
		for iteration in [100, 200, 400, 600, 800, 1000]:
			print("POPULATION::", population, "   ITERATION::", iteration)
			print(bbo(MAX_EMIGRATION, MAX_IMMIGRATION, MAX_MUTATION, iteration, population)['fitness'])
		print("----------------")

################################################
	print("\n\n#######################################################################################\n",\
	      "######################################################################################\n\n")
################################################
	POPULATION = 50
	ITERATIONS = 150

	Desc2 = '''
	POPULATION = 50
	ITERATIONS = 150
	
	They are fixed.
	we change only immigration, mutation, emigration.
	'''
	print(Desc2, '\n\n')

	print("**       Our solution:: \n")
	print(normal(POPULATION))
	print("\n--------------------------------------------------------------------\n\n\n")

	print("**       Our bbo:: \n")
	print(bbo(MAX_EMIGRATION, MAX_IMMIGRATION, MAX_MUTATION, ITERATIONS, POPULATION)['fitness'])
	print("\n--------------------------------------------------------------------\n\n\n")

	print("\n                             =====MUTATION=====\n")
	for mutation in (0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1):
		print("MUTATION::", mutation)
		print(bbo(MAX_EMIGRATION, MAX_IMMIGRATION, mutation, ITERATIONS, POPULATION)['fitness'])
		print("")

	print("----------------")

	print("\n                             =====EMIGRATION=====\n")
	for emigration in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1):
		print("EMIGRATION", emigration)
		print(bbo(emigration, MAX_IMMIGRATION, MAX_MUTATION, ITERATIONS, POPULATION)['fitness'])
		print("")

	print("----------------")

	print("\n                             =====IMMIGRATION=====\n")
	for immigration in (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1):
		print("IMMIGRATION", immigration)
		print(bbo(MAX_EMIGRATION, immigration, MAX_MUTATION, ITERATIONS, POPULATION)['fitness'])
		print("")


