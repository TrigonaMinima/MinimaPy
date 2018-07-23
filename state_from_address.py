import re
import difflib
import pandas as pd


nonjunk_red = re.compile(r"\b\w+\b")
pin_reg = re.compile(r"\b[0-9]{6}\b")


CITIES = set(["MUMBAI", "DELHI", "BANGALORE", "HYDERABAD", "AHMEDABAD", "CHENNAI", "KOLKATA", "SURAT", "PUNE", "JAIPUR", "LUCKNOW", "KANPUR", "NAGPUR", "VISAKHAPATNAM", "INDORE", "THANE", "BHOPAL", "PIMPRI-CHINCHWAD", "PATNA", "VADODARA", "GHAZIABAD", "LUDHIANA", "COIMBATORE", "AGRA", "MADURAI", "NASHIK", "FARIDABAD", "MEERUT", "RAJKOT", "KALYAN-DOMBIVALI", "VASAI-VIRAR", "VARANASI", "SRINAGAR", "AURANGABAD", "DHANBAD", "AMRITSAR", "NAVI MUMBAI", "ALLAHABAD", "RANCHI", "HOWRAH (CITY AREA)", "JABALPUR", "GWALIOR", "VIJAYAWADA", "JODHPUR", "RAIPUR", "KOTA[22]", "GUWAHATI", "CHANDIGARH", "SOLAPUR", "HUBBALLI-DHARWAD", "TIRUCHIRAPPALLI", "BAREILLY", "MYSORE", "TIRUPPUR", "GURGAON", "ALIGARH", "JALANDHAR", "BHUBANESWAR", "SALEM", "MIRA-BHAYANDAR", "WARANGAL", "THIRUVANANTHAPURAM", "GUNTUR", "BHIWANDI", "SAHARANPUR", "GORAKHPUR", "BIKANER", "AMRAVATI", "NOIDA", "JAMSHEDPUR", "BHILAI", "CUTTACK", "FIROZABAD", "KOCHI", "NELLORE[26]", "BHAVNAGAR", "DEHRADUN", "DURGAPUR", "ASANSOL", "NANDED", "KOLHAPUR", "AJMER", "AKOLA", "GULBARGA", "JAMNAGAR", "UJJAIN", "LONI", "SILIGURI", "JHANSI", "ULHASNAGAR", "JAMMU", "SANGLI-MIRAJ & KUPWAD", "MANGALORE", "ERODE[27]", "BELGAUM", "AMBATTUR", "TIRUNELVELI", "MALEGAON", "GAYA", "JALGAON", "UDAIPUR", "MAHESHTALA", "DAVANAGERE", "KOZHIKODE", "KURNOOL", "RAJPUR SONARPUR", "RAJAHMUNDRY[28][29]", "BOKARO", "SOUTH DUMDUM", "BELLARY", "PATIALA", "GOPALPUR", "AGARTALA", "BHAGALPUR", "MUZAFFARNAGAR", "BHATPARA", "PANIHATI", "LATUR", "DHULE", "TIRUPATI[30]", "ROHTAK", "KORBA", "BHILWARA", "BERHAMPUR", "MUZAFFARPUR", "AHMEDNAGAR", "MATHURA", "KOLLAM", "AVADI", "KADAPA", "KAMARHATI", "SAMBALPUR", "BILASPUR", "SHAHJAHANPUR", "SATARA", "BIJAPUR", "RAMPUR", "SHIVAMOGGA", "CHANDRAPUR", "JUNAGADH", "THRISSUR", "ALWAR", "BARDHAMAN", "KULTI", "KAKINADA", "NIZAMABAD", "PARBHANI", "TUMKUR", "KHAMMAM", "OZHUKARAI", "BIHAR SHARIF",
              "PANIPAT", "DARBHANGA", "BALLY", "AIZAWL", "DEWAS", "ICHALKARANJI", "KARNAL", "BATHINDA", "JALNA", "ELURU", "KIRARI SULEMAN NAGAR", "BARASAT", "PURNIA", "SATNA", "MAU", "SONIPAT", "FARRUKHABAD", "SAGAR", "ROURKELA", "DURG", "IMPHAL", "RATLAM", "HAPUR", "ARRAH", "KARIMNAGAR", "ANANTAPUR", "ETAWAH", "AMBERNATH", "NORTH DUMDUM", "BHARATPUR", "BEGUSARAI", "NEW DELHI", "GANDHIDHAM", "BARANAGAR", "TIRUVOTTIYUR", "PUDUCHERRY", "SIKAR", "THOOTHUKUDI", "REWA", "MIRZAPUR", "RAICHUR", "PALI", "RAMAGUNDAM[34]", "HARIDWAR", "VIJAYANAGARAM", "KATIHAR", "NAGARCOIL", "SRI GANGANAGAR", "KARAWAL NAGAR", "MANGO", "THANJAVUR", "BULANDSHAHR", "ULUBERIA", "MURWARA", "SAMBHAL", "SINGRAULI", "NADIAD", "SECUNDERABAD", "NAIHATI", "YAMUNANAGAR", "BIDHAN NAGAR", "PALLAVARAM", "BIDAR", "MUNGER", "PANCHKULA", "BURHANPUR", "RAURKELA INDUSTRIAL TOWNSHIP", "KHARAGPUR", "DINDIGUL", "GANDHINAGAR", "HOSPET", "NANGLOI JAT", "ENGLISH BAZAR", "ONGOLE", "DEOGHAR", "CHAPRA", "HALDIA", "KHANDWA", "NANDYAL", "CHITTOOR[35]", "MORENA", "AMROHA", "BHIND", "BHALSWA JAHANGIR PUR", "MADHYAMGRAM", "BHIWANI", "NAVI MUMBAI PANVEL RAIGAD", "BAHARAMPUR", "AMBALA", "MORVI", "FATEHPUR", "RAE BARELI", "KHORA", "BHUSAWAL", "ORAI", "BAHRAICH", "VELLORE", "MAHESANA", "SAMBALPUR", "RAIGANJ", "SIRSA", "DANAPUR", "SERAMPORE", "SULTAN PUR MAJRA", "GUNA", "JAUNPUR", "PANVEL", "SHIVPURI", "SURENDRANAGAR DUDHREJ", "UNNAO", "HUGLI AND CHINSURAH", "ALAPPUZHA", "KOTTAYAM", "MACHILIPATNAM", "SHIMLA", "ADONI", "UDUPI", "TENALI", "PRODDATUR", "SAHARSA", "HINDUPUR", "SASARAM", "HAJIPUR", "BHIMAVARAM", "DEHRI", "MADANAPALLE", "SIWAN", "BETTIAH", "GUNTAKAL", "SRIKAKULAM", "MOTIHARI", "DHARMAVARAM", "GUDIVADA", "NARASARAOPET", "SURYAPET", "BAGAHA", "TADIPATRI", "KISHANGANJ", "KARAIKUDI", "MIRYALAGUDA", "JAMALPUR", "KAVALI", "TADEPALLIGUDEM", "AMARAVATI", "BUXAR", "JEHANABAD", "AURANGABAD",
              "DWARKA", "MOHALI", "ROHINI", "GANGTOK", "FIROZPUR", "PORBANDAR", "HOSHIARPUR", "FEROZPUR", "MANDI", "DAMAN", "BHUJ", "SHILLONG", ])

STATES = set([
    "ANDHRA PRADESH", "ARUNACHAL PRADESH", "ASSAM", "BIHAR", "GOA",
    "GUJARAT", "HARYANA", "HIMACHAL PRADESH", "JAMMU & KASHMIR",
    "KARNATAKA", "KERALA", "MADHYA PRADESH", "MAHARASHTRA", "MANIPUR",
    "MEGHALAYA", "MIZORAM", "NAGALAND", "ORISSA", "PUNJAB", "RAJASTHAN",
    "SIKKIM", "TAMIL NADU", "TRIPURA", "UTTAR PRADESH", "WEST BENGAL",
    "CHHATTISGARH", "UTTARAKHAND", "JHARKHAND", "TELANGANA", "DELHI",
    "ANDAMAN & NICOBAR ISLANDS", "CHANDIGARH", "DADRA & NAGAR HAVELI",
    "DADRA NAGAR HAVELI", "DAMAN & DIU", "DAMAN DIU", "DAMAN AND DIU",
    "LAKSHADWEEP", "PUDUCHERRY", "ANDAMAN NICOBAR ISLANDS",
    "ANDAMAN AND NICOBAR ISLANDS"
])


def clean(x):
    x = nonjunk_red.findall(str(x).upper())
    return x


def ngrams(x, n=2):
    return [" ".join(x[i:i + n]) for i in range(len(x) - n + 1)]


def get_part_of_addr(x, area_list):
    bigrams = ngrams(x)
    trigrams = ngrams(x, 3)
    words_final = x + bigrams + trigrams

    parts = []
    for word in words_final:
        if word in area_list:
            parts.append(word)

    if not parts:
        for word in words_final:
            for area in area_list:
                if difflib.SequenceMatcher(None, word, area).ratio() > 0.93:
                    parts.append(area)

    return "|".join(set(parts))


def get_pin(x):
    x = str(x)
    if x:
        return "|".join(pin_reg.findall(x))
    elif x or x is None:
        return ""


def read_data(file, sheet=None):
    if sheet is None:
        df = pd.read_excel(file)
    else:
        df = pd.read_excel(file, sheet_name=sheet)
    print("Read", file)
    return df


def add_cols(df, addr_col):
    addr_clean = addr_col[:5] + "_CLEAN"
    state_col = addr_col[:5] + "_STATE"
    city_col = addr_col[:5] + "_CITY"
    pin_col = addr_col[:5] + "_PIN"

    df[addr_clean] = df[addr_col].apply(clean)
    print("\tClean done")
    df[state_col] = df[addr_clean].apply(get_part_of_addr, args=(STATES,))
    print("\tStates extracted")
    df[city_col] = df[addr_clean].apply(get_part_of_addr, args=(CITIES,))
    print("\tCities extracted")
    df[pin_col] = df[addr_col].apply(get_pin)
    print("\tPINs extracted")

    return df


def save_data(out_file, df):
    df.to_excel(out_file, index=False)
    print("Saved -", out_file)


if __name__ == "__main__":
    addr_cols = []
    files = []
    sheets = ["Sheet1", ]

    for file in files:
        for sheet in sheets:
            df = read_data(file, sheet)
            for col in addr_cols:
                print(col)
                if col in df.columns:
                    df = add_cols(df, col)
                out_file = sheet + ".xlsx"
                save_data(out_file, df)

            # out_file = sheet.replace(".xlsx", "_state.xlsx")
