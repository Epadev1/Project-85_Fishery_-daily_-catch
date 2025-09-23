#PROJECT 85: Fishery daily Catch
#integers
#Quantities of fish caught each day in kg
#print("#1. INTEGER\n")
dailyfish=[10,15,20,25,30,40]
total= sum(dailyfish)
print("The total of all fish caught daily  is: ",total,"kg")
average=total/len(dailyfish)
print("the average of fish caught daily is: ",average,"kg")
minimumcatch=min(dailyfish)
print("the minimum quantity of fish caught daily is: ",minimumcatch,"kg")
maximumcatch=max(dailyfish)
print("the maximum quantity of fish caught daily is:",maximumcatch,"kg")

# report for fishery daily catch
#print("#2. STRING\n")
report=(
    f"Fishery Daily Report:\n"
        f"Total Catch:{total} kg\n"
        f"Average Daily catch:{average}kg\n")
print(report)

#boolean
#print("#3. BOOLEAN\n")

threshold=30
if average> threshold:
    print("status:It is above standard\n\n")
else:
    print("status:It is below standard\n\n")

#lists:modify and sort daily_catch list.
#print("#4. LIST\n")
dailyfish=[10,5,15,20,25,30,40]
print("daily fish caught before modification\n",dailyfish)
dailyfish.append(50)
if 15 in dailyfish:
    dailyfish.remove(15)

dailyfish.sort()
print(" after being modified and sorted catch list",dailyfish)

#array module
#print("#5. ARRAY\n")
import array
fdailycatch= array.array('i',[20,22,40,70])
arraytotal=sum(fdailycatch)
print(f"\nthe total quantity in array is:{arraytotal}kg")
print(f"\nArray total:{arraytotal}kg vs List total:{sum(dailyfish)}kg\n")

#dictionaries: list of fish caught daily records
#print("#6. DICTIONARY\n")
fishery_daily_catch=[
    {'id':1,'name':'tilapia','value':20},
    {'id':2,'name':'jellyfish','value':30},
    {'id':3,'name':'catfish','value':45},
    {'id':4,'name':'tunafish','value':38},            

    ]
print("Original list of fish caught daily:",fishery_daily_catch)
   #update record
fishery_daily_catch[2]['value']=15
del fishery_daily_catch[0]
total=sum(rec['value'] for rec in fishery_daily_catch)
print("updated")

for record in fishery_daily_catch:
    print(record)
print("total value",total,"kg")



 
 










