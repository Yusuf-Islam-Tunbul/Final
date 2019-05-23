import numpy as np
import matplotlib.pyplot as plt

def get_path(n):
  l = list(range(n))
  np.random.shuffle(l)
  l.remove(5)
  return l

def get_path_length(gene):
    total_length=np.sum(distances[gene[1:],gene[:-1]])    
    return total_length

def draw_path(newgene):
    x_coordinates_r,y_coordinates_r=list(y_coordinates[newgene]),list(x_coordinates[newgene])
    plt.plot(x_coordinates_r,y_coordinates_r,linewidth=0.6)

def cross_over(gene1,gene2, mutation=0.5):
    
  r = np.random.randint(len(gene1))
  newgene = np.append(gene1[:r],gene2[r:])
    
  missing = set(gene1)-set(newgene)
  elements, count = np.unique(newgene, return_counts=True)
  duplicates = elements[count==2]
  duplicate_indices=(newgene[:, None] == duplicates).argmax(axis=0)
  
  newgene[duplicate_indices]=list(missing)
  
  if np.random.rand()<mutation:
    i1,i2 = np.random.randint(0,len(newgene),2)
    newgene[[i1,i2]] = newgene[[i2,i1]]
    
  newgene=np.hstack(([5],newgene,[5]))  
  return newgene

def create_initial_population(m):
  population = []
  fitness = []
  for i in range(m):
    gene1,gene2=get_path(81),get_path(81)
    gene=cross_over(gene1,gene2,mutation=0.5)
    path_length = get_path_length(gene)
    
    population.append(gene)
    fitness.append(path_length)
  
  population = np.array(population)
  fitness = np.array(fitness)  
  sortedindex = np.argsort(fitness)
  return population[sortedindex], fitness[sortedindex]

def next_generation(population):
  pop = []
  fit = []
  f=int(np.sqrt(len(population)))
  for gene1 in population[:f]:
    for gene2 in population[:f]:
      x =  cross_over(gene1,gene2,mutation=0.5)
      l = get_path_length(x)
      pop.append(x)
      fit.append(l)
  
  population = np.array(pop)
  fitness = np.array(fit)  
  sortedindex = np.argsort(fitness)
  return population[sortedindex], fitness[sortedindex]

population,fitness=create_initial_population(10000) 

for i in range(1000000):
    population,fitness=next_generation(population)
    
draw_path(population[0])
plt.imshow(map, extent=[26,45,35.5,42.5])
plt.axes().set_aspect(1.3,'datalim')
print(fitness[0])