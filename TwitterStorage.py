import json

class TwitterStorage:

    def __init__(self, config):
        try:
            f= open(config['filename'])
            self.data= json.load(f)
            self.config= config
            self.config['default_since_id']= 1
            self.config['default_replied_users']= []
            f.close()
        except(FileNotFoundError):
            print("Storage file doesn't exists. Creating new file")
            f= open(config['filename'],'w')
            f.write("[]")
            f.close()
            f= open(config['filename'],'r')
            self.data= json.load(f)
            f.close()
    
    def createUnit(self,post_id):
        self.data.append({
            "post_id":post_id,
            "since_id":self.config['default_since_id'],
            "replied_users":self.config['default_replied_users']
            })
    def showData(self):
        print(type(self.data))
        print(self.data)

    def getRepliedUsers(self, post_id):
        entry = next((item for item in self.data if item["post_id"] == post_id), None)
        if entry is None:
            return None
        else:
            return entry['replied_users']

    def getSinceId(self, post_id):
        entry= next((item for item in self.data if item["post_id"] == post_id), None)
        if entry is None:
            return None
        else:
            return entry['since_id']

    def setSinceId(self,post_id,since_id):
        for d in self.data:
            if d['post_id']== post_id:
                d['since_id']= since_id
    
    def setRepliedUser(self,post_id, replied_users):
        for d in self.data:
            if d['post_id']== post_id:
                d['replied_users'].extend(replied_users)

    def save(self):
        with open(self.config['filename'], 'w') as f:
            json.dump(self.data, f, indent=4)

if __name__ == '__main__':
    config= {}
    config['filename']= 'data.json'
    s= TwitterStorage(config)
    # print(s.getRepliedUsers(3))
    # print(s.getSinceId(3))
    print(s.setSinceId(3,7))
    # print(s.setRepliedUser(3,['shivam','mattoo','umangkoul']))
    s.createUnit(5)
    s.showData()
    s.save()

