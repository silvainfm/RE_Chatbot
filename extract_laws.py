import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape from
url = 'https://legimonaco.mc/~~write/explorer/type=legislation/tncNature=loi/dateDesc'

# maybe get different urls and let;s focus on real estate laws
urls =['https://cms.law/fr/mco/publication/reforme-fiscale-en-matiere-de-mutations-immobilieres', 
 'https://cms.law/fr/mco/publication/amelioration-de-la-gestion-locative-du-bien-commercial-ou-d-habitation',
 'https://cms.law/fr/mco/publication/reforme-de-la-copropriete', 
 'https://cms.law/fr/mco/publication/le-caractere-engageant-de-l-offre-de-vente-ou-d-achat-en-matiere-immobiliere-a-monaco', 
 'https://cms.law/fr/mco/publication/projets-de-constructions-dans-le-secteur-protege',
 'https://cms.law/fr/mco/publication/investissement-immobilier-transition-energetique',
 'https://cms.law/fr/mco/publication/refinancement-immobilier',
 'https://lobservateurdemonaco.com/infos/marchands-de-biens-bouleversements-2022/',
 'https://www.benjaminpratt.com/fr/news/monaco-les-lois-de-immobilier-locatif', 
 'https://ageprim.com/fr/actualites/monaco/loi-887/#:~:text=Toute%20personne%20souhaitant%20mettre%20en,pendant%20plus%20de%20cinq%20ans.',
 'https://www.valeri-agency.com/fr/pages/habitation-monaco-lois-1235-1291-887.html',
 'https://journaldemonaco.gouv.mc/Journaux/2021/Journal-8570/Loi-n-1.514-du-10-decembre-2021-portant-modification-de-certaines-dispositions-de-la-loi-n-1.357-du-19-fevrier-2009-definissant-le-contrat-habitation-capitalisation-dans-le-secteur-domanial-modifiee', 
 'https://www.99avocats.com/publications/adoption-de-la-proposition-de-loi-n-252-relative-a-lencadrement-de-la-profession-de-marchand-de-biens',
 'https://legimonaco.mc/tnc/loi/2011/06-29-1.381/']

'''I have a list of urls that contain information about real estate laws in Monaco, in French. I know French so no need for translation. 
I want to build a database from the information in these urls, to have a chatbot answer questions about real estate laws. 
For that I want to structure the data as follows: {'input ': 'question', 'output': 'answer'}. The db will be a json file. 
I want you to take the information in these urls, and add it to the data, in the format given.
Let me know when you are ready for the urls. '''

# The structure of our data will be the following:
{"input": "What color is the sky?", "output": "The sky is blue."}
{"input": "Where is the best place to get cloud GPUs?", "output": "Brev.dev"}

# Connect to the website and fetch the page
response = requests.get(url)

# Check for a valid response
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Assuming the data is in a table, find the table element
    table = soup.find('table', {'class': 'your_table_class'})  # replace 'your_table_class' with the actual class name
    
    if table:
        # Iterate through each row in the table
        for row in table.find_all('tr')[1:]:  # skipping the header row
            columns = row.find_all('td')
            # Do something with the data, e.g., print it or save it to a file
            print([column.text for column in columns])
else:
    print(f'Failed to retrieve page with status code: {response.status_code}')

def parse_subpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract and print data from subpage
        # (replace with your actual data extraction logic)
        data = soup.find('div', {'class': 'your_data_class'}).text
        print(data)
    else:
        print(f'Failed to retrieve subpage {url} with status code: {response.status_code}')

def main():
    url = 'https://legimonaco.mc/~~write/explorer/type=legislation/tncNature=loi/dateDesc'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Assuming the links to subpages are in anchor tags with a specific class
        links = soup.find_all('a', {'class': 'your_link_class'})  
        
        for link in links:
            subpage_url = link['href']
            if subpage_url.startswith('/'):  # If the URL is relative
                subpage_url = f'https://legimonaco.mc{subpage_url}'  # Convert to absolute URL
            parse_subpage(subpage_url)
    else:
        print(f'Failed to retrieve page with status code: {response.status_code}')

#if __name__ == '__main__':
    #main()
