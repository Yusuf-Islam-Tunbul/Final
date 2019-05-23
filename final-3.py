import itertools as iter

AK=[0,6,30,32,14,45,79,31] #32
EGE=[47,8,34,19,63,42,44,2] #63
İAD=[5,41,25,65,57,39,50,67,49,37,17,69,70] #5
DAD=[43,11,29,64,75,3,48,12,23,22,74,35,61,24] #48
GAD=[20,62,46,26,1,55,78,71,72] #62
MAR=[9,15,33,16,53,76,40,10,21,58,38] #76
KAR=[13,80,66,77,4,36,73,56,18,54,59,51,27,28,68,60,52,7] #4

#FINDING ORDER OF REGIONS#

regions=[32,63,48,62,76,4]
        
perms=list(iter.permutations(regions,6))

distance=99999

for i in (perms):
    temp_order=[5]+list(i)+[5]
    temp_distance=np.sum(distances[temp_order[1:],temp_order[:-1]])
    if temp_distance<distance:
        distance=temp_distance
        order=temp_order
        
#order of regions is İAD-MAR-EGE-AK-GAD-DAD-KAR-İAD#

total_distance_r=0

İAD_=İAD
İAD_.remove(5)
region_distance=99999
for i in range(100000):
    np.random.shuffle(İAD_)
    İAD__=[5]+İAD_+[10]
    temp_region_distance=np.sum(distances[İAD__[1:],İAD__[:-1]])
    if temp_region_distance<region_distance:
        region_distance=temp_region_distance
        İAD___=İAD__
total_distance_r+=region_distance

MAR_=MAR
MAR_.remove(10)
region_distance=99999
for i in range(100000):
    np.random.shuffle(MAR_)
    MAR__=[10]+MAR_+[42]
    temp_region_distance=np.sum(distances[MAR__[1:],MAR__[:-1]])
    if temp_region_distance<region_distance:
        region_distance=temp_region_distance
        MAR___=MAR__
total_distance_r+=region_distance

EGE_=EGE
EGE_.remove(42)
region_distance=99999
for i in range(100000):
    np.random.shuffle(EGE_)
    EGE__=[42]+EGE_+[31]
    temp_region_distance=np.sum(distances[EGE__[1:],EGE__[:-1]])
    if temp_region_distance<region_distance:
        region_distance=temp_region_distance
        EGE___=EGE__
total_distance_r+=region_distance      
          
AK_=AK
AK_.remove(31)
region_distance=99999
for i in range(100000):
    np.random.shuffle(AK_)
    AK__=[31]+AK_+[26]
    temp_region_distance=np.sum(distances[AK__[1:],AK__[:-1]])
    if temp_region_distance<region_distance:
        region_distance=temp_region_distance
        AK___=AK__        
total_distance_r+=region_distance 
      
GAD_=GAD
GAD_.remove(26)
region_distance=99999
for i in range(100000):
    np.random.shuffle(GAD_)
    GAD__=[26]+GAD_+[48]
    temp_region_distance=np.sum(distances[GAD__[1:],GAD__[:-1]])
    if temp_region_distance<region_distance:
        region_distance=temp_region_distance
        GAD___=GAD__  
total_distance_r+=region_distance
                
DAD_=DAD
DAD_.remove(48)
region_distance=99999
for i in range(100000):
    np.random.shuffle(DAD_)
    DAD__=[48]+DAD_+[7]
    temp_region_distance=np.sum(distances[DAD__[1:],DAD__[:-1]])
    if temp_region_distance<region_distance:
        region_distance=temp_region_distance
        DAD___=DAD__  
total_distance_r+=region_distance
        
KAR_=KAR
KAR_.remove(7)
region_distance=999999
for i in range(100000):
    np.random.shuffle(KAR_)
    KAR__=[7]+KAR_+[5]
    temp_region_distance=np.sum(distances[KAR__[1:],KAR__[:-1]])
    if temp_region_distance<region_distance:
        region_distance=temp_region_distance
        KAR___=KAR__          
total_distance_r+=region_distance

route=İAD___[:-1]+MAR___[:-1]+EGE___[:-1]+AK___[:-1]+GAD___[:-1]+DAD___[:-1]+KAR___

plt.imshow(map, extent=[26,45,35.5,42.5])
plt.axes().set_aspect(1.3,'datalim')
x_coordinates_r,y_coordinates_r=list(y_coordinates[route]),list(x_coordinates[route])
plt.plot(x_coordinates_r,y_coordinates_r,linewidth=0.6)
plt.text(27.5,34.7,'The total distance covered is %a km' %int(total_distance_r))
plt.savefig('image2',dpi=300)