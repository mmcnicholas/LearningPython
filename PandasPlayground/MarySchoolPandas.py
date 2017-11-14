import pandas as pd
from pprint import pprint
from time import time

stringystring = """School Name 
Grades
School District 
County
City
ACADEMY FOR GLOBAL CITIZENSHIP
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACE TECHNICAL CHARTER HIGH SCHOOL
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - BARTOLOME DE LAS CASAS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - BRIGHTON PARK CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - CARLOS FUENTES CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - ESMERALDA SANTIAGO CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - JOVITA IDAR
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - MAJOR HECTOR P GARCIA MD CAMPUS
(8-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - OCTAVIO PAZ CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - OFFICER DONALD J MARQUEZ CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - PFC OMAR E TORRES CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - RUFINO TAMAYO CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK - SPC DANIEL ZIZUMBO CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK- SANDRA CISNEROS CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NETWORK VICTORIA SOTO CAMPUS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NEWTWORK - ROBERTO CLEMENTE CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ACERO CHTR SCH NEWTWORK- SOR JUANA INES DE LA CRUZ
(K-11)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
AMANDLA CHARTER SCHOOL
(6-12)
AMANDLA CHARTER SCHOOL
(COOK)
CHICAGO
ASIAN HUMAN SERVICES -PASSAGE CHRTR
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ASPIRA CHARTER - BUSINESS AND FINANCE HS
(9-11)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ASPIRA CHARTER - EARLY COLLEGE PREP HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ASPIRA CHARTER - HAUGAN CAMPUS
(6-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
BARBARA A SIZEMORE CAMPUS
(K-8)
BETTY SHABAZZ INTERNATIONAL CHARTER SCHOOL
(COOK)
CHICAGO
BETTY SHABAZZ INTERNATIONAL CHARTER SCHOOL
(K-8)
BETTY SHABAZZ INTERNATIONAL CHARTER SCHOOL
(COOK)
CHICAGO
BRONZEVILLE ACADEMY CHARTER SCHOOL
(K-8)
CHICAGO LIGHTHOUSE CHARTER SCHOOL
(COOK)
CHICAGO
CAMBRIDGE LAKES CHARTER SCHOOL
(K-12)
CUSD 300
(KANE)
PINGREE GROVE
CATALYST CHARTER - MARIA ES
(K-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CATALYST CHARTER-CIRCLE ROCK ES
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CHICAGO COLLEGIATE CHARTER SCHOOL
(4-9)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CHICAGO MATH & SCI ELEM CHARTER
(6-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CHICAGO VIRTUAL CHARTER SCHOOL
(K-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CHRISTOPHER HOUSE CHRT ES
(K-5)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - AVALON/SOUTH SHORE
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - BASIL CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - BOND CAMPUS
(K-6)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - BUCKTOWN CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - IRVING PARK CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - LONGWOOD CAMPUS
(3-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - LOOMIS PRIMARY CAMPUS
(K-2)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - NORTHTOWN CAMPUS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - PRAIRIE CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - QUEST NORTH CAMPUS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - RALPH ELLISON CAMPUS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - WASHINGTON PK CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - WEST BELDEN CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
CICS - WRIGHTWOOD
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
EPIC ACADEMY HIGH SCHOOL
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
ERIE ELEM CHARTER SCHOOL
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
FOUNDATIONS COLLEGE PREP CHARTER
(6-9)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
FRAZIER PREP ACAD CHARTER ES
(PK-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
GALAPAGOS ROCKFORD CHARTER SCH
(K-8)
ROCKFORD SD 205
(WINNEBAGO)
ROCKFORD
GREAT LAKES ACADEMY CHARTER ES
(K-4)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
HORIZON SCI ACADEMY - SOUTHWEST CHARTER
(K-11)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
HORIZON SCIENCE ACAD-BELMONT CHARTER SCH
(K-8)
HORIZON SCIENCE ACAD-BELMONT
(COOK)
CHICAGO
HORIZON SCIENCE ACAD-MCKINLEY PARK CHARTER SCH
(K-12)
HORIZON SCIENCE ACAD-MCKINLEY PARK
(COOK)
CHICAGO
IHSCA CHARTER HIGH SCHOOL
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
INTRINSIC CHARTER HIGH SCHOOL
(7-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
JACKSON CHARTER SCHOOL
(K-8)
ROCKFORD SD 205
(WINNEBAGO)
ROCKFORD
KIPP ACADEMY CHICAGO CAMPUS
(5-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
KIPP CHICAGO CHARTER SCHOOL - KIPP ONE ACADEMY
(K-1,5-6)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
KIPP CHICAGO CHARTERS - ASCEND ACADEMY
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
KIPP CHICAGO CHARTERS - BLOOM CAMPUS
(5-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LEARN 10 CHARTER SCHOOL
(K-3)
NORTH CHICAGO SD 187
(LAKE)
NORTH CHICAGO
LEARN CHARTER 9 CAMPUS IN WAUKEGAN
(K-5)
LEARN 9 CAMPUS IN WAUKEGAN
(LAKE)
WAUKEGAN
LEARN CHARTER EXCEL CAMPUS
(K-5)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LEARN CHARTER SCH 6 NORTH CHICAGO CAMPUS
(K-8)
NORTH CHICAGO SD 187
(LAKE)
GREAT LAKES
LEARN CHTR - 7TH CAMPUS
(PK-5)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LEARN CHTR - BUTLER
(PK-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LEARN CHTR - HUNTER PERKINS CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LEARN CHTR - MIDDLE SCHOOL
(6-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LEARN CHTR - SOUTH CHICAGO CAMPUS
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LEARN CHTR-CAMPBELL CAMPUS
(K-5)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LEGACY ACAD OF EXCELLENCE CHARTER SCH
(K-12)
ROCKFORD SD 205
(WINNEBAGO)
ROCKFORD
LEGACY ELEM CHARTER SCHOOL
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LEGAL PREP ACADEMY CHARTER HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
LOCKE A ELEM CHARTER ACADEMY
(PK-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
MONTESSORI OF ENGLEWOOD CHTR ES
(PK-7)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
MOVING EVEREST CHARTER SCHOOL
(K-3)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NAMASTE ELEM CHARTER SCHOOL
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NKRUMAH ACADEMY CHARTER ES
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR - MANSUETO
(9-10)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR RAUNER COLLEGE PREP
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-BAKER CAMPUS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-BUTLER COLLEGE PREP - CRIMSON
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-CHICAGO BULLS PREP
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-COMER COLLEGE PREP
(6-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-DRW TRADING COLLEGE PREP
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-GOLDER COLLEGE PREP
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-HANSBERRY COLLEGE PREP - SILVER
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-ITW SPEER ACAD
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-JOHNSON COLLEGE PREP
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-MUCHIN COLLEGE PREP
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-NOBLE CAMPUS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-PRITZKER COLLEGE PREP
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-ROWE-CLARK MS ACAD
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-THE NOBLE ACADEMY
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NOBLE ST CHTR-UIC COLLEGE PREP
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NORTH LAWNDALE PREP CHTR - CHRISTIANA
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
NORTH LAWNDALE PREP CHTR-COLLINS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
PERSPECTIVES CHTR - HIGH SCHOOL OF TECHNOLOGY
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
PERSPECTIVES CHTR - IIT CAMPUS
(6-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
PERSPECTIVES CHTR - JOSLIN CAMPUS
(6-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
PERSPECTIVES CHTR - LEADERSHIP ACAD
(6-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
POLARIS ELEM CHARTER ACADEMY
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
PRAIRIE CROSSING CHARTER SCHOOL
(K-8)
PRAIRIE CROSSING CHARTER SCHOOL
(LAKE)
GRAYSLAKE
PROVIDENCE-ENGLEWOOD ELEM CHARTER
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
QUEST CHARTER SCHOOL ACADEMY
(5-12)
PEORIA SD 150
(PEORIA)
PEORIA
ROBERTSON CHARTER SCHOOL
(K-8)
DECATUR SD 61
(MACON)
DECATUR
ROWE ELEMENTARY
(K-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
SIU CHARTER SCH OF EAST ST LOUIS
(9-12)
EAST ST LOUIS SD 189
(ST. CLAIR)
EAST SAINT LOUIS
SOUTHLAND COLLEGE PREP CHARTER HIGH SCHOOL
(9-12)
SOUTHLAND COLLEGE PREP
(COOK)
RICHTON PARK
SPRINGFIELD BALL CHARTER SCHOOL
(K-8)
SPRINGFIELD SD 186
(SANGAMON)
SPRINGFIELD
UNIV OF CHICAGO CHTR - WOODSON
(7-8)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
UNIV OF CHICAGO CHTR-DONOGHUE
(K-5)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
UNIV OF CHICAGO CHTR-NTH KENWOOD
(PK-5)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
UNIV OF CHICAGO CHTR-WOODLAWN
(6-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
URBAN PREP CHTR ACAD BRONZEVILLE HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
URBAN PREP CHTR ACAD ENGLEWOOD HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
URBAN PREP CHTR ACAD WEST CAMPUS HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YBMC CHARTER SCH
(11-12)
MCLEAN COUNTY USD 5
(MCLEAN)
NORMAL
YCCS CHTR - CHATHAM
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS- MCKINLEY-LAKESIDE LEADERSHIP ACADEMY
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-ALBIZU CAMPUS PUERTO RICAN HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-ASPIRA PANTOJA ALT HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-ASSOC HSE EL CUARTO ANO HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-AUSTIN CAREER ED CNTR HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-CCA ACADEMY HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-COMMUNITY YOUTH DEV INST HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-INNOVATIONS OF ARTS INTEGR HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-JANE ADDAMS ALTERNATIVE HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-LATINO YOUTH ALTERNATIVE HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-OLIVE HARVEY MID COLLEGE HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-PROGRESSIVE LEADERSHIP ACADEMY
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-SCHOLASTIC ACHIEVEMENT HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-SULLIVAN HOUSE ALT HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-TRUMAN MIDDLE COLLEGE HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-WEST TOWN ACADEMY ALT HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-WESTSIDE HOLISTIC LDR ACAD HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YCCS-YOUTH CONNECTION LEADERSHIP ACADEMY
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO
YOUNG WOMENS LEADERSHIP CHARTR HS
(9-12)
CITY OF CHICAGO SD 299
(COOK)
CHICAGO"""

col_number = 5

pprint(stringystring)
school_dict = {}
i = 5
sting_list = stringystring.split('\n')
listlist = []
for x in range(5):
    listlist.append([])


while i < len(sting_list):
    if sting_list[i] != '':
        listlist[i % col_number].append(sting_list[i])
    i+=1

print(len(listlist[0]))
print(len(listlist[1]))
print(len(listlist[2]))
print(len(listlist[3]))
print(len(listlist[4]))

for i in range(col_number):
    school_dict[sting_list[i]] = listlist[i]
df = pd.DataFrame(
    school_dict
)

print(df)
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()