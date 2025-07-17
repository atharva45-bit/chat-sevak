def get_bot_response(message):
    msg = message.lower()
    # Voting rights & Election
    if 'vote' in msg or 'voting' in msg:
        return 'The legal voting age in India is 18 years. Every citizen above 18 has the right to vote. To register, visit the National Voters Service Portal (nvsp.in).'
    if 'voter id' in msg:
        return 'You can apply for a Voter ID online at the National Voters Service Portal (nvsp.in). It is required for voting in elections.'
    if 'election commission' in msg:
        return 'The Election Commission of India is an autonomous body that administers election processes in India at national and state levels.'
    if 'electoral roll' in msg:
        return 'The electoral roll is a list of all eligible voters in a constituency. You can check your name on the roll at nvsp.in.'
    # Major Government Schemes
    if 'pmay' in msg or 'pradhan mantri awas yojana' in msg:
        return 'Pradhan Mantri Awas Yojana (PMAY) provides affordable housing to the urban and rural poor.'
    if 'ujjwala' in msg:
        return 'Pradhan Mantri Ujjwala Yojana provides LPG connections to women from below poverty line households.'
    if 'jan dhan' in msg:
        return 'Pradhan Mantri Jan Dhan Yojana aims to expand affordable access to financial services such as bank accounts, remittances, credit, insurance, and pensions.'
    if 'ayushman' in msg or 'pmjay' in msg:
        return 'Ayushman Bharat (PM-JAY) is a health insurance scheme for economically vulnerable Indians, providing coverage up to ₹5 lakh per family per year.'
    if 'kisan samman' in msg or 'pm kisan' in msg:
        return 'PM-KISAN provides income support of ₹6,000 per year to all farmer families in India, paid in three equal installments.'
    if 'mudra' in msg:
        return 'Pradhan Mantri Mudra Yojana (PMMY) provides loans up to ₹10 lakh to non-corporate, non-farm small/micro enterprises.'
    if 'skill india' in msg:
        return 'Skill India Mission aims to train over 40 crore people in India in different skills by 2022.'
    if 'digital india' in msg:
        return 'Digital India is a campaign to improve online infrastructure and increase internet connectivity to make the country digitally empowered.'
    if 'make in india' in msg:
        return 'Make in India is an initiative to encourage companies to manufacture their products in India and incentivize dedicated investments into manufacturing.'
    if 'startup india' in msg:
        return 'Startup India is a flagship initiative to build a strong ecosystem for nurturing innovation and Startups in the country.'
    if 'swachh bharat' in msg:
        return 'Swachh Bharat Mission aims to clean up the streets, roads, and infrastructure of India’s cities and rural areas.'
    if 'beti bachao' in msg or 'beti padhao' in msg:
        return 'Beti Bachao, Beti Padhao aims to generate awareness and improve the efficiency of welfare services intended for girls in India.'
    if 'atma nirbhar' in msg:
        return 'Atma Nirbhar Bharat (Self-Reliant India) is a vision to make India self-reliant through various reforms and incentives.'
    if 'national health mission' in msg:
        return 'National Health Mission (NHM) aims to provide accessible, affordable, and quality health care to the rural population.'
    if 'mid day meal' in msg:
        return 'The Mid Day Meal Scheme provides free lunches to school children on working days in government and government-aided schools.'
    if 'old age pension' in msg:
        return 'The Indira Gandhi National Old Age Pension Scheme provides social assistance to the elderly below the poverty line.'
    if 'pension' in msg:
        return 'The government offers various pension schemes like Atal Pension Yojana, National Pension System (NPS), and old age pension schemes.'
    if 'ration card' in msg:
        return 'Ration cards are issued to households eligible to purchase subsidized food grain from the Public Distribution System under the National Food Security Act.'
    if 'scholarship' in msg:
        return 'There are various government scholarships for students, such as the National Scholarship Portal (NSP), Post Matric Scholarship, and more.'
    if 'public scheme' in msg or 'scheme' in msg:
        return 'There are many public schemes in India: PMAY (housing), Ujjwala (LPG), Jan Dhan (banking), Ayushman Bharat (health), PM-KISAN (farmers), Mudra (loans), Skill India, Digital India, and more. Please specify the scheme for details.'
    # Judiciary & Important Laws
    if 'supreme court' in msg:
        return 'The Supreme Court of India is the highest judicial court and the final court of appeal under the Constitution of India.'
    if 'high court' in msg:
        return 'High Courts are the principal civil courts of original jurisdiction in each state and union territory.'
    if 'public interest litigation' in msg or 'pil' in msg:
        return 'Public Interest Litigation (PIL) allows any individual or group to file a petition in the Supreme Court or High Courts for the protection of public interest.'
    if 'habeas corpus' in msg:
        return 'Habeas Corpus is a writ requiring a person under arrest to be brought before a judge or court, ensuring protection against unlawful detention.'
    if 'landmark judgment' in msg or 'important judgment' in msg:
        return 'Some landmark Supreme Court judgments include Kesavananda Bharati v. State of Kerala (basic structure doctrine), Maneka Gandhi v. Union of India (right to life and liberty), and Vishaka v. State of Rajasthan (sexual harassment guidelines).'
    if 'basic structure' in msg:
        return 'The Basic Structure Doctrine, established in Kesavananda Bharati v. State of Kerala (1973), holds that certain features of the Constitution cannot be altered by amendment.'
    if 'article 21' in msg:
        return 'Article 21 of the Constitution guarantees the protection of life and personal liberty to every person.'
    if 'article 32' in msg:
        return 'Article 32 gives the right to constitutional remedies, allowing individuals to approach the Supreme Court for enforcement of fundamental rights.'
    if 'article 370' in msg:
        return 'Article 370 granted special autonomous status to the state of Jammu and Kashmir. It was abrogated in August 2019.'
    if 'ipc' in msg or 'indian penal code' in msg:
        return 'The Indian Penal Code (IPC) is the official criminal code of India, covering all substantive aspects of criminal law.'
    if 'crpc' in msg or 'criminal procedure code' in msg:
        return 'The Code of Criminal Procedure (CrPC) is the main legislation on procedure for administration of substantive criminal law in India.'
    if 'right to information' in msg or 'rti' in msg:
        return 'The Right to Information Act (RTI) empowers citizens to seek information from public authorities, promoting transparency and accountability.'
    if 'right to education' in msg or 'rte' in msg:
        return 'The Right to Education Act (RTE) makes education a fundamental right for children aged 6 to 14 years.'
    if 'dowry prohibition' in msg:
        return 'The Dowry Prohibition Act, 1961 prohibits the giving or receiving of dowry in India.'
    if 'posco' in msg:
        return 'The Protection of Children from Sexual Offences (POCSO) Act, 2012 is a comprehensive law to provide protection to children from sexual offences.'
    if 'sc/st act' in msg:
        return 'The Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989 aims to prevent atrocities and hate crimes against SC/ST communities.'
    if 'nda' in msg and 'alliance' in msg:
        return 'NDA stands for National Democratic Alliance, a coalition of political parties in India.'
    # Constitution
    if 'constitution' in msg or 'constitutional' in msg:
        return 'The Constitution of India is the supreme law of India. It lays down the framework demarcating fundamental political code, structure, procedures, powers, and duties of government.'
    if 'fundamental right' in msg:
        return 'Fundamental Rights in India include Right to Equality, Freedom, Against Exploitation, to Freedom of Religion, Cultural and Educational Rights, and Constitutional Remedies.'
    if 'directive principle' in msg:
        return 'Directive Principles of State Policy are guidelines for the framing of laws by the government, aimed at ensuring social and economic democracy.'
    if 'fundamental duty' in msg:
        return 'Fundamental Duties are moral obligations of all citizens to help promote a spirit of patriotism and to uphold the unity of India.'
    if 'preamble' in msg:
        return 'The Preamble to the Constitution of India declares India to be a Sovereign, Socialist, Secular, Democratic Republic and aims to secure justice, liberty, equality, and fraternity for its citizens.'
    if 'article' in msg:
        return 'The Constitution of India has 448 articles in 25 parts. Please specify the article number for details.'
    # Default
    return 'Sorry, I can help with queries about government schemes, judiciary, public schemes, and constitutional laws. Please ask a specific question.'