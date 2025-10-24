#creating a function that does simple math for the percentage of SH and the general cost

TGC = 100 #total gallon capacity of the tank
P_solution = input('input percentage of SH (Sodium Hypchlorite) listed on the bottle')
GS = input('input the volume of liquid listed on the bottle')
materials = ['stucco', 'vinyl', 'painted wood', 'metal', 'shingle', 'brick']
staintypes = ['material', 'biotic']
severity = ['light', 'medium', 'heavy']

p_needed = input(f"input material to be washed: {materials}, stain type (biotic, abiotic): {staintypes}, and severity of stains: {severity}")
mforfunc = {"stucco": 6, "vinyl": 2, "painted wood": 2, "metal": 3, "brick": 4}
ppp = 0
endp = []



def FTS(P_needed, P_solution, GS): #finds total solution needed for gallons needed 
    global ppp
    newlist = P_needed.split()
    commonsM = list(set(newlist).intersection(set(materials)))
    commonsT = list(set(newlist).intersection(set(staintypes)))
    commonsS = list(set(newlist).intersection(set(severity)))
    for bombo in mforfunc:
        if bombo in commonsM:
            ppp = mforfunc[bombo]
            
            
            
    
    




def find_division(x,y,z):
    print(z)
    y = x/z
    return(y)








FTS(p_needed,P_solution, GS)
print(f"mix: {find_division(float(P_solution),endp,ppp)} total gallons including SH.")