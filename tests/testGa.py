if __name__ == '__main__':
	from algorithms.ga.ga import Ga
	from benchmarks.time import MAX_GA_CROSS_OVER, MAX_GA_MUTATION

	POPULATION = 50
	ITERATIONS = 150

	Desc = '''
		POPULATION = 50
		ITERATIONS = 150

		They are fixed.
		we change only Cross_Rate, Mutation_Rate.\n
		
		Ga(new_population, new_Generations, new_Cross_Rate, new_Muta_Rate)
	'''
	print(Desc, '\n\n')

	print("**       Our Ga:: \n")
	print(Ga(POPULATION, ITERATIONS, MAX_GA_CROSS_OVER, MAX_GA_MUTATION)['fitness'])
	print("\n--------------------------------------------------------------------\n\n\n")

	print("\n                             =====CROSS_OVER=====\n")
	for cross in (0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.97):
		print("CROSS OVER::", cross)
		print(Ga(POPULATION, ITERATIONS, cross, MAX_GA_MUTATION)['fitness'])
		print("----------------")

	print("\n                             =====MUTATION=====\n")
	for mutation in (0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1):
		print("MUTATION::", mutation)
		print(Ga(POPULATION, ITERATIONS, MAX_GA_CROSS_OVER, mutation)['fitness'])
		print("----------------")

	################################################
	print("\n\n#######################################################################################\n", \
	      "######################################################################################\n\n")
	################################################

	Desc1 = """
			for this first part of the test, we fix AX_EMIGRATION, MAX_IMMIGRATION, MAX_MUTATION
			(see the time.py), and play on the iterations and population size.
		"""

	print(Desc1)

	for population in [50, 100, 150, 200]:
		for iteration in [100, 200, 400, 600, 800, 1000]:
			print("POPULATION::", population, "   ITERATION::", iteration)
			print(Ga(population, iteration, MAX_GA_CROSS_OVER, MAX_GA_MUTATION)['fitness'])
			print("----------------")
