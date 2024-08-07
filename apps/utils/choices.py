# titles
MR = 'Mr'
MRS = 'Mrs'
MISS = 'Miss'
DR = 'Dr'
ER = 'Er'

# invite status choices
INVITE_STATUS = (
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('declined', 'Declined'),
)

TITLE_TYPE = (
    (MR, MR),
    (MRS, MRS),
    (MISS, MISS),
    (DR, DR),
    (ER, ER),
)


# identity
CITIZENSHIP = 'Citizenship'
LICENSE = 'License'
PAN_ID = 'pan_id'
VOTER_ID = 'voter_id'
NATIONAL_CARD = 'national_card'
PASSPORT = 'passport'
IDENTITY_TYPE = (
    (CITIZENSHIP, CITIZENSHIP),
    (LICENSE, LICENSE),
    (PAN_ID, PAN_ID),
    (VOTER_ID, VOTER_ID),
    (NATIONAL_CARD, NATIONAL_CARD),
    (PASSPORT, PASSPORT),
)

# skill status
STATUS = (
    ("Active", "Active"),
    ("InActive", "InActive"),
)

# job types
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
    ('Freelance', 'Freelance'),
    ('Temporary', 'Temporary'),
    ('Volunteer', 'Volunteer'),
    ('Other', 'Other'),
)

# job working_preferences
WORKING = (
    ('Remote', 'Remote'),
    ('On site', 'On site')
)

# marital status
MARTIAL_STATUS = (
    ("Single", "Single"),
    ("Married", "Married"),
)



# order status
ORDER_STATUS = (
    ("New", "New"),
    ("Cancelled", "Cancelled"),
    ("In Progress", "In Progress"),
    ("Cancelled by Admin", "Cancelled by Admin"),
    ("Ready to Pickup", "Ready to Pickup"),
    ("Delivered", "Delivered"),
    ("Completed", "Completed"),
)

# payment status
PAYMENT_STATUS = (
    ("Success", "Success"),
    ("Failed", "Failed")
)

# ADDRESS TYPES
ADDRESS_TYPES = (
    ("Billing", "Billing"),
    ("Shipping", "Shipping")
)

# jobpost applicant status
JOBPOST_STATUS = (
    ("Pending", "Pending"),  # inital status
    ("Shortlisted", "Shortlisted"),  # short_listed status
    ("Selected", "Selected"),  # selected status
    ("Rejected", "Rejected"),  # not selected status
    ("Process", "Process"),  # after processing status
)

# lang proficiency status
PROFICIENCY_STATUS = (
    ("No", "No"),
    ("Basic", "Basic"),
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced")
)

# countries
COUNTRIES = (
    ("AFGHANISTAN", "AFGHANISTAN"),
    ("ALBANIA", "ALBANIA"),
    ("ALGERIA", "ALGERIA"),
    ("AMERICAN SAM0A", "AMERICAN SAM0A"),
    ("ANDORRA", "ANDORRA"),
    ("ANGOLA", "ANGOLA"),
    ("ANGUILLA", "ANGUILLA"),
    ("ANTARCTICA", "ANTARCTICA"),
    ("ANTIGUA AND BARBUDA", "ANTIGUA AND BARBUDA"),
    ("ARGENTINA", "ARGENTINA"),
    ("ARMENIA", "ARMENIA"),
    ("ARUBA", "ARUBA"),
    ("AUSTRALIA", "AUSTRALIA"),
    ("AUSTRIA", "AUSTRIA"),
    ("AZERBAIJAN", "AZERBAIJAN"),
    ("BAHAMAS", "BAHAMAS"),
    ("BAHRAIN", "BAHRAIN"),
    ("BANGLADESH", "BANGLADESH"),
    ("BARBADOS", "BARBADOS"),
    ("BELARUS", "BELARUS"),
    ("BELGIUM", "BELGIUM"),
    ("BELIZE", "BELIZE"),
    ("BENIN", "BENIN"),
    ("BERMUDA", "BERMUDA"),
    ("BHUTAN", "BHUTAN"),
    ("BOLIVIA", "BOLIVIA"),
    ("BOSNIA AND HERZEGOVINA", "BOSNIA AND HERZEGOVINA"),
    ("BOTSWANA", "BOTSWANA"),
    ("BOUVET ISLAND", "BOUVET ISLAND"),
    ("BRAZIL", "BRAZIL"),
    ("BRITISH INDIAN OCEAN TERRITORY", "BRITISH INDIAN OCEAN TERRITORY"),
    ("BRUNEI", "BRUNEI"),
    ("BULGARIA", "BULGARIA"),
    ("BURKINA FASO", "BURKINA FASO"),
    ("BURUNDI", "BURUNDI"),
    ("CAMBODIA", "CAMBODIA"),
    ("CAMEROON", "CAMEROON"),
    ("CANADA", "CANADA"),
    ("CAPE VERDE", "CAPE VERDE"),
    ("CAYMAN ISLANDS", "CAYMAN ISLANDS"),
    ("CENTRAL AFRICAN REPUBLIC", "CENTRAL AFRICAN REPUBLIC"),
    ("CHAD", "CHAD"),
    ("CHILE", "CHILE"),
    ("CHINA", "CHINA"),
    ("CHRISTMAS ISLAND", "CHRISTMAS ISLAND"),
    ("COCOS (KEELING) ISLANDS", "COCOS (KEELING) ISLANDS"),
    ("COLOMBIA", "COLOMBIA"),
    ("COMOROS", "COMOROS"),
    ("CONGO", "CONGO"),
    ("THE DEMOCRATIC REPUBLIC OF CONGO", "THE DEMOCRATIC REPUBLIC OF CONGO"),
    ("COOK ISLANDS", "COOK ISLANDS"),
    ("COSTA RICA", "COSTA RICA"),
    ("IVORY COAST", "IVORY COAST"),
    ("CROATIA", "CROATIA"),
    ("CUBA", "CUBA"),
    ("CYPRUS", "CYPRUS"),
    ("CZECH REPUBLIC", "CZECH REPUBLIC"),
    ("DENMARK", "DENMARK"),
    ("DJIBOUTI", "DJIBOUTI"),
    ("DOMINICA", "DOMINICA"),
    ("DOMINICAN REPUBLIC", "DOMINICAN REPUBLIC"),
    ("EAST TIMOR", "EAST TIMOR"),
    ("ECUADOR", "ECUADOR"),
    ("EGYPT", "EGYPT"),
    ("ENGLAND", "ENGLAND"),
    ("EL SALVADOR", "EL SALVADOR"),
    ("EQUATORIAL GUINEA", "EQUATORIAL GUINEA"),
    ("ERITREA", "ERITREA"),
    ("ESTONIA", "ESTONIA"),
    ("ETHIOPIA", "ETHIOPIA"),
    ("FALKLAND ISLANDS", "FALKLAND ISLANDS"),
    ("FAROE ISLANDS", "FAROE ISLANDS"),
    ("FIJI ISLANDS", "FIJI ISLANDS"),
    ("FINLAND", "FINLAND"),
    ("FRANCE", "FRANCE"),
    ("FRENCH GUIANA", "FRENCH GUIANA"),
    ("FRENCH POLYNESIA", "FRENCH POLYNESIA"),
    ("FRENCH SOUTHERN TERRITORIES", "FRENCH SOUTHERN TERRITORIES"),
    ("GABON", "GABON"),
    ("GAMBIA", "GAMBIA"),
    ("GEORGIA", "GEORGIA"),
    ("GERMANY", "GERMANY"),
    ("GHANA", "GHANA"),
    ("GIBRALTAR", "GIBRALTAR"),
    ("GREECE", "GREECE"),
    ("GREENLAND", "GREENLAND"),
    ("GRENADA", "GRENADA"),
    ("GUADELOUPE", "GUADELOUPE"),
    ("GUAM", "GUAM"),
    ("GUATEMALA", "GUATEMALA"),
    ("GUERNSEY", "GUERNSEY"),
    ("GUINEA", "GUINEA"),
    ("GUINEA-BISSAU", "GUINEA-BISSAU"),
    ("GUYANA", "GUYANA"),
    ("HAITI", "HAITI"),
    ("HEARD ISLAND AND MCDONALD ISLANDS", "HEARD ISLAND AND MCDONALD ISLANDS"),
    ("HOLY SEE (VATICAN CITY STATE)", "HOLY SEE (VATICAN CITY STATE)"),
    ("HONDURAS", "HONDURAS"),
    ("HONG KONG", "HONG KONG"),
    ("HUNGARY", "HUNGARY"),
    ("ICELAND", "ICELAND"),
    ("INDIA", "INDIA"),
    ("INDONESIA", "INDONESIA"),
    ("IRAN", "IRAN"),
    ("IRAQ", "IRAQ"),
    ("IRELAND", "IRELAND"),
    ("ISRAEL", "ISRAEL"),
    ("ISLE OF MAN", "ISLE OF MAN"),
    ("ITALY", "ITALY"),
    ("JAMAICA", "JAMAICA"),
    ("JAPAN", "JAPAN"),
    ("JERSEY", "JERSEY"),
    ("JORDAN", "JORDAN"),
    ("KAZAKHSTAN", "KAZAKHSTAN"),
    ("KENYA", "KENYA"),
    ("KIRIBATI", "KIRIBATI"),
    ("KUWAIT", "KUWAIT"),
    ("KYRGYZSTAN", "KYRGYZSTAN"),
    ("LAOS", "LAOS"),
    ("LATVIA", "LATVIA"),
    ("LEBANON", "LEBANON"),
    ("LESOTHO", "LESOTHO"),
    ("LIBERIA", "LIBERIA"),
    ("LIBYAN ARAB JAMAHIRIYA", "LIBYAN ARAB JAMAHIRIYA"),
    ("LIECHTENSTEIN", "LIECHTENSTEIN"),
    ("LITHUANIA", "LITHUANIA"),
    ("LUXEMBOURG", "LUXEMBOURG"),
    ("MACAO", "MACAO"),
    ("NORTH MACEDONIA", "NORTH MACEDONIA"),
    ("MADAGASCAR", "MADAGASCAR"),
    ("MALAWI", "MALAWI"),
    ("MALAYSIA", "MALAYSIA"),
    ("MALDIVES", "MALDIVES"),
    ("MALI", "MALI"),
    ("MALTA", "MALTA"),
    ("MARSHALL ISLANDS", "MARSHALL ISLANDS"),
    ("MARTINIQUE", "MARTINIQUE"),
    ("MAURITANIA", "MAURITANIA"),
    ("MAURITIUS", "MAURITIUS"),
    ("MAYOTTE", "MAYOTTE"),
    ("MEXICO", "MEXICO"),
    ("MICRONESIA, FEDERATED STATES OF", "MICRONESIA, FEDERATED STATES OF"),
    ("MOLDOVA", "MOLDOVA"),
    ("MONACO", "MONACO"),
    ("MONGOLIA", "MONGOLIA"),
    ("MONTSERRAT", "MONTSERRAT"),
    ("MONTENEGRO", "MONTENEGRO"),
    ("MOROCCO", "MOROCCO"),
    ("MOZAMBIQUE", "MOZAMBIQUE"),
    ("MYANMAR", "MYANMAR"),
    ("NAMIBIA", "NAMIBIA"),
    ("NAURU", "NAURU"),
    ("NEPAL", "NEPAL"),
    ("NETHERLANDS", "NETHERLANDS"),
    ("NETHERLANDS ANTILLES", "NETHERLANDS ANTILLES"),
    ("NEW CALEDONIA", "NEW CALEDONIA"),
    ("NEW ZEALAND", "NEW ZEALAND"),
    ("NICARAGUA", "NICARAGUA"),
    ("NIGER", "NIGER"),
    ("NIGERIA", "NIGERIA"),
    ("NIUE", "NIUE"),
    ("NORFOLK ISLAND", "NORFOLK ISLAND"),
    ("NORTH KOREA", "NORTH KOREA"),
    ("NORTHERN IRELAND", "NORTHERN IRELAND"),
    ("NORTHERN MARIANA ISLANDS", "NORTHERN MARIANA ISLANDS"),
    ("NORWAY", "NORWAY"),
    ("OMAN", "OMAN"),
    ("PAKISTAN", "PAKISTAN"),
    ("PALAU", "PALAU"),
    ("PALESTINE", "PALESTINE"),
    ("PANAMA", "PANAMA"),
    ("PAPUA NEW GUINEA", "PAPUA NEW GUINEA"),
    ("PARAGUAY", "PARAGUAY"),
    ("PERU", "PERU"),
    ("PHILIPPINES", "PHILIPPINES"),
    ("PITCAIRN", "PITCAIRN"),
    ("POLAND", "POLAND"),
    ("PORTUGAL", "PORTUGAL"),
    ("PUERTO RICO", "PUERTO RICO"),
    ("QATAR", "QATAR"),
    ("REUNION", "REUNION"),
    ("ROMANIA", "ROMANIA"),
    ("RUSSIAN FEDERATION", "RUSSIAN FEDERATION"),
    ("RWANDA", "RWANDA"),
    ("SAINT HELENA", "SAINT HELENA"),
    ("SAINT KITTS AND NEVIS", "SAINT KITTS AND NEVIS"),
    ("SAINT LUCIA", "SAINT LUCIA"),
    ("SAINT PIERRE AND MIQUELON", "SAINT PIERRE AND MIQUELON"),
    ("SAINT VINCENT AND THE GRENADINES", "SAINT VINCENT AND THE GRENADINES"),
    ("SAMOA", "SAMOA"),
    ("SAN MARINO", "SAN MARINO"),
    ("SAO TOME AND PRINCIPE", "SAO TOME AND PRINCIPE"),
    ("SAUDI ARABIA", "SAUDI ARABIA"),
    ("SCOTLAND", "SCOTLAND"),
    ("SENEGAL", "SENEGAL"),
    ("SERBIA", "SERBIA"),
    ("SEYCHELLES", "SEYCHELLES"),
    ("SIERRA LEONE", "SIERRA LEONE"),
    ("SINGAPORE", "SINGAPORE"),
    ("SLOVAKIA", "SLOVAKIA"),
    ("SLOVENIA", "SLOVENIA"),
    ("SOLOMON ISLANDS", "SOLOMON ISLANDS"),
    ("SOMALIA", "SOMALIA"),
    ("SOUTH AFRICA", "SOUTH AFRICA"),
    ("SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
        "SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS"),
    ("SOUTH KOREA", "SOUTH KOREA"),
    ("SOUTH SUDAN", "SOUTH SUDAN"),
    ("SPAIN", "SPAIN"),
    ("SRI LANKA", "SRI LANKA"),
    ("SUDAN", "SUDAN"),
    ("SURINAME", "SURINAME"),
    ("SVALBARD AND JAN MAYEN", "SVALBARD AND JAN MAYEN"),
    ("SWAZILAND", "SWAZILAND"),
    ("SWEDEN", "SWEDEN"),
    ("SWITZERLAND", "SWITZERLAND"),
    ("SYRIA", "SYRIA"),
    ("TAJIKISTAN", "TAJIKISTAN"),
    ("TANZANIA", "TANZANIA"),
    ("THAILAND", "THAILAND"),
    ("TIMOR-LESTE", "TIMOR-LESTE"),
    ("TOGO", "TOGO"),
    ("TOKELAU", "TOKELAU"),
    ("TONGA", "TONGA"),
    ("TRINIDAD AND TOBAGO", "TRINIDAD AND TOBAGO"),
    ("TUNISIA", "TUNISIA"),
    ("TURKEY", "TURKEY"),
    ("TURKMENISTAN", "TURKMENISTAN"),
    ("TURKS AND CAICOS ISLANDS", "TURKS AND CAICOS ISLANDS"),
    ("TUVALU", "TUVALU"),
    ("UGANDA", "UGANDA"),
    ("UKRAINE", "UKRAINE"),
    ("UNITED ARAB EMIRATES", "UNITED ARAB EMIRATES"),
    ("UNITED KINGDOM", "UNITED KINGDOM"),
    ("UNITED STATES", "UNITED STATES"),
    ("UNITED STATES MINOR OUTLYING ISLANDS",
        "UNITED STATES MINOR OUTLYING ISLANDS"),
    ("URUGUAY", "URUGUAY"),
    ("UZBEKISTAN", "UZBEKISTAN"),
    ("VANUATU", "VANUATU"),
    ("VENEZUELA", "VENEZUELA"),
    ("VIETNAM", "VIETNAM"),
    ("VIRGIN ISLANDS, BRITISH", "VIRGIN ISLANDS, BRITISH"),
    ("VIRGIN ISLANDS, U.S.", "VIRGIN ISLANDS, U.S."),
    ("WALES", "WALES"),
    ("WALLIS AND FUTUNA", "WALLIS AND FUTUNA"),
    ("WESTERN SAHARA", "WESTERN SAHARA"),
    ("YEMEN", "YEMEN"),
    ("ZAMBIA", "ZAMBIA"),
    ("ZIMBABWE", "ZIMBABWE"),
)
