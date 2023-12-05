export interface BookStateModel {
    sampleBooks: Book[];
    userRatedBooks: Book[];
    similarUserBooks: Book[];
    recommendedBooks: Book[];
    popularBooks: Book[];
}

export interface Book {
    isbn: number,
    title: string,
    year_of_publication: string,
    author: string,
    publisher: string,
    img: string
}

export interface Rating {
    userId: string,
    isbn: string,
    rating: number
}