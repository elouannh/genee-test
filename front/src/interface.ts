
export interface IPlace {
    departement: string,
    commune: string,
    desc: string
}

export default interface ICase {
    id: number,
    name: string,
    places: IPlace[]
}
