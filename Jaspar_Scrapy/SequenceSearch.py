import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

# Insert FASTA sequence in Scan function and run it.
class SequenceSearch():
    def sequencesearch(self):
        driver = webdriver.Chrome()
        driver.get("https://jaspar.genereg.net/search?page_size=250&tax_group=vertebrates&q=Homo+sapiens&collection=CORE") # Link input must be changed for each page
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/h4/a").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/textarea").send_keys(""">hub_3671779_hs1_hub_3671779_catLiftOffGenesV1_PRNP-203 range=chr20:4723586-4740802 5'pad=0 3'pad=0 strand=+ repeatMasking=none
tcttctcaactgacaccccaaacataatggggcagaatcaagtccccgct
gtgcctgtccagctccctggcttaaacaatccattggcataataaaatgg
tagttgttttaaaccacctaagttgtggggtatttgcagcacatcagtaa
taaccagaataggtcataagtcaatcccctttggttccctagttctttcc
ctccaagaaatcccaggccatttgagccctttcctgatgggaggaaagca
gtcgaccagaaaatacgattcttttgaggaaaagatgggttttagcgtct
tggaaccaagcttcacagagcgccttctgccagtgggcagccagcccctt
gcctaggctgatctggtcacctacttccagccccaccccagctctgtcct
cccacccagctctgtcctccctgcaggccctgagcctctaggagactcaa
agagacactgtgctgcccgctgaattcatctcccagtgagccatctctga
ggaaaggaggtaaggctctgaatgcgatgtcaacctaagcattacataac
actgataggttgtaaaatggcctcgctgcctagtgctcattctaactggc
cacaatccagtcctccctgttgcactgagtcagctccctccaaaggcggc
gctttccaggcctcctggttgccctttcccagcagacctttcaagtgctc
acccacactcacataaacatggcccaggcactgtttacagcagctctcct
ctgtgcattctcctggcttctcctgtctctcgccatttgtacccctcccc
tgcaacttgagtgacagtgattggtcctgagatgcaaatatttgatgcac
atatgtttacaatgcagcctcagcttttttttttttttttgtaaagagac
aaagagtgagacagggtcttggcctatagccctgtggcccaggctggagt
gcagtggcacaattaaagctcactgcagcctctacctcctgggctcaagc
aatcctcccatctcagcctccccagtagctgggactacaggactgtgcca
ccgttcccagcaattttttttattttttgtagaaatggggtctcactatg
ttgctcactctggtctcaaactcctgagctcaagcaatcttcctgccttg
gcctctgaaagtgctgggattacaggcctgagccactgcacctggctgtc
aacattcttaaatctctttccttacatgcttcctaaacctctcacccaaa
actaggagactagatgtcctattttccccagggcatgcctggtttacgcc
catttcactttaaaagtgcccaatttgggtaataatttataagatccccc
tccctctaaatcctgtccttctatcacttcatccttcgctctcctttaaa
atgagacagttgtcagcaggaatcctgcgcaagaacacaccaccctgttt
catagaagatatctcaggtaatgtgcaaacacgggtttttaaacggagcg
catttttctcatttgttaatatcaccacctaaatcatctcttgcctaaaa
caaggagtagaaagtgaatgaaggaaggaacaggtgatggtcagtgtcct
ttctacgcctcaaaatttaagagtttatgtgaaaattcataaatattaat
ctcaatccaggttaagcaaaattttttgctctcctctttagaaatttctg
gttgccaaagttccagaaattgcttcctcattcctgagcctttcattttc
tcgatttctccattatgtaacggggagctggagctttgggccgaatttcc
aattaaagatgatttttacagtcaatgagccacgtcagggagcgatggca
cccgcaggcggtatcaactgatgcaagtgttcaagcgaatctcaactcgt
tttttccggtgactcattcccggccctgcttggcagcgctgcacccttta
acttaaacctcggccggccgcccgccgggggcacagagtgtgcgccgggc
CGCGCGGCAATTGGTCCCCGCGCCGACCTCCGCCCGCGAGCGCCGCCGCT
TCCCTTCCCCGCCCCGCGTCCCTCCCCCTCGGCCCCGCGCGTCGCCTGTC
CTCCGAGCCAGTCGCTGACAGCCGCGGCGCCGCGAGCTTCTCCTCTCCTC
ACGACCGAGgcaggtaaacgcccggggtgggaggaacgcgggcgggggca
ggggagccgcgggggccgagtgaggaccccgggcctcgggtcccaggcgc
aagggtgcccggccgggcggggtcgggaccccagtgaggaggggccgggg
gctgccccgcgggcgcgtgacgcgtctcgggcctgcccggctgcgctggt
ctccgctcgggtgaggcggcttggcttcgcttttcaggttaggaaagctc
cctttactgcgcgttggggggctgggggagctggcggagccccgttaggg
aggtcggtggcgccggggtgtctcagcgccccctgcaccccgcgcgggtc
cggcccagcgggcgatcgctggcgcccagggaactccgggagggccgcca
gcgggctccgcagggcgcggggcggggaggggcgcctgggggccgcgggg
ctcgcgctccccgcccgttggccgcccctcggaggccgagatcggggccc
agaacgccccttggcaaggcctggcgcttccgcgatgcccagagggtgct
tggggggatggagagaggggcgcccgccgggggagttccgggagcctcgg
tgcctcccgccgcagctgcagcgttcctcccgggaggcggcccagccctt
catcctcgccgcctgagcttctccgaggggggccgcagccttgcggccgt
tgccaccgcctggagaagcggcc""")
                                                                                                                                                   
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/button").click()
        time.sleep(2)

        # After scan, expose all profiles 

        dropdown = driver.find_element(By.XPATH, "/html/body/div/div[1]/section[2]/div/div[1]/div/div[2]/div[3]/div[1]/label/select")
        dropdown.click()
        dropdown.send_keys("All")

        time.sleep(10)

        # Collect data

        element = driver.find_element(By.ID, "search_table")
        html_content = element.get_attribute('outerHTML')


        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table")
        
        
        df_full = pd.read_html(str(table))[0]
        df_full.to_csv("tfs_page4_80")
        print(df_full)


seq = SequenceSearch()
seq.sequencesearch()
