from utils.mongoconfig import connect_client


class PlaceService:
    @staticmethod
    def get_towns_by_dep(dep_name: str) -> list[str]:
        client = connect_client();

        db = client['refer']
        col = db['values']

        docs = []

        for doc in col.find({ 'DEP_NOM': dep_name }):
            docs.append(doc['COM_NOM'])

        return docs

    @staticmethod
    def get_dep_by_town(town_name: str) -> list[str]:
        client = connect_client();

        db = client['refer']
        col = db['values']

        return col.find_one({ 'COM_NOM': town_name })['DEP_NOM']