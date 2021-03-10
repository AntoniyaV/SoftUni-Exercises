class Storage:
    categories = []
    topics = []
    documents = []

    def __repr__(self):
        documents = '\n'.join(doc.__repr__() for doc in self.documents)
        return documents

    @staticmethod
    def get_element(id, collection):
        element = [el for el in collection if el.id == id]
        return element[0]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.get_element(category_id, self.categories)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.get_element(topic_id, self.topics)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.get_element(document_id, self.documents)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.get_element(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_element(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.get_element(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.get_element(document_id, self.documents)
        return document
