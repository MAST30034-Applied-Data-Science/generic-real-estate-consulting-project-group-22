
import urllib.request
import os


urlretrieve= urllib.request.urlretrieve
raw_data_dir='data/raw/'

# download population dataset
url= f"https://www.abs.gov.au/statistics/people/population/regional-population/2021/32180DS0001_2001-21.xlsx"
output_dir=f"{raw_data_dir}population.xlsx"
urlretrieve(url, output_dir) 
print("end population")

# download income rate dataset
url= f"https://www.abs.gov.au/statistics/labour/jobs/jobs-australia/2014-15-2018-19/61600DS0001_2018-19.xlsx"
output_dir=f"{raw_data_dir}income.xlsx"
urlretrieve(url, output_dir) 
print("end income rate")

# download unemployment rate dataset
url= f"https://www.nationalskillscommission.gov.au/sites/default/files/2022-06/SALM%20Smoothed%20SA2%20Datafiles%20%28ASGS%202016%29%20-%20March%20quarter%202022.csv"
output_dir=f"{raw_data_dir}unemployment.csv"
urlretrieve(url, output_dir) 
print("end unemployment")

# download school locations dataset
url= f"https://www.education.vic.gov.au/Documents/about/research/datavic/dv331_schoollocations2022.csv"
output_dir=f"{raw_data_dir}school.csv"
urlretrieve(url, output_dir) 
print("end school")

# download postcode dataset
url= f"https://www.matthewproctor.com/Content/postcodes/australian_postcodes.csv"
output_dir=f"{raw_data_dir}postcode.csv"

# this website denies access with web crawler like urlretrieve
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(url,output_dir)

print("end postcode")








