class CommentaryRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "text": "Why earth is round?", "category": "positive"},
            {"id": 2, "text": "Astana and Almaty", "category": "positive"},
            {"id": 3, "text": ":KJSLl;akfoaofn;falsd;k", "category": "negative"},
            {"id": 4, "text": "Kazahstan akfapwk kd;afkpawm akw","category": "negative"},
            {"id": 5, "text": ":LK ;laksl;dkwa l;jasl;djwa;o", "category": "positive"},
        ]

    def get_all(self):
        return self.comments[::-1]

    def get_one(self, comment_id):
        for comment in self.comments:
            if comment["id"] == comment_id:
                return comment
        return None

    def save(self, comment):
        if "id" not in comment or not comment["id"]:
            comment["id"] = self.get_next_id()
        self.comments.append(comment)
        return comment

    def get_next_id(self):
        return len(self.comments) + 1