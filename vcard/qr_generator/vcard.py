class VCard:
    def __init__(self) -> None:
        self.prefix = "BEGIN:VCARD \n VERSION:3.0"
        self.name = "N:{}"
        self.fname = "FN:{}"
        self.org = "ORG:{}"
        self.title = "TITLE:{}"
        self.addr = "ADR:;;{}"
        self.phone = "TEL;WORK;VOICE;CELL:{}"
        self.email = "EMAIL;WORK;INTERNET:{}"
        self.website = "URL:{}"
        self.suffix = "END:VCARD"
        
    def gen_name(self, name):
        if name is not None and name != "":
            s = name.replace(" ", ";")
            return self.name.format(s)
        else:
            return None
        
    def gen_fname(self, name):
        if name is not None and name != "":
            return self.fname.format(name)
        else:
            return None
    
    def gen_organization(self, org):
        if org is not None and org != "":
            return self.org.format(org)
        else:
            return None
    
    def gen_title(self, title):
        if title is not None and title != "":
            return self.title.format(title)
        else:
            return None
    
    def gen_address(self, address):
        if address is not None and address != "":
            addr = address.replace(",", ";")
            return self.addr.format(addr)
        else:
            return None
        
    def gen_phone(self, phone):
        if phone is not None and phone != "":
            return self.phone.format(phone)
        else:
            return None
    
    def gen_email(self, email):
        if email is not None and email != "":
            return self.email.format(email)
        else:
            return None
        
    def gen_website(self, website):
        if website is not None and website != "":
            return self.website.format(website)
        else:
            return None
        
    def generate_vcard(self, **kwargs):
        name = kwargs['name'] if 'name' in kwargs.keys() else None
        organization = kwargs['company'] if 'company' in kwargs.keys() else None
        title = kwargs['title'] if 'title' in kwargs.keys() else None
        address = kwargs['address'] if 'address' in kwargs.keys() else None
        phone = kwargs['phone'] if 'phone' in kwargs.keys() else None
        email = kwargs['email'] if 'email' in kwargs.keys() else None
        website = kwargs['website'] if 'website' in kwargs.keys() else None
        
        
        name = self.gen_name(name)
        fname = self.gen_fname(name)
        org = self.gen_organization(organization)
        title = self.gen_title(title)
        address = self.gen_address(address)
        phone = self.gen_phone(phone)
        email = self.gen_email(email)
        website = self.gen_website(website)
        vcard_list = [
            self.prefix, 
            name, 
            fname, 
            org, 
            title,
            address,
            email, 
            phone, 
            website, 
            self.suffix]
        vcard_list = [i for i in vcard_list if i is not None]
        vcard = "\n".join(vcard_list)
        print(vcard)
        return vcard
        
        
        