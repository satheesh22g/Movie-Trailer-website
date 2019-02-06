import media
import fresh_tomatoes
infinity=media.Movie('Man Who Know infinity','HD Trailer',
                     'https://images-na.ssl-images-amazon.com/images/I/A1X%2Bu9vdXtL._SY445_.jpg',
                     'https://www.youtube.com/watch?v=oXGm9Vlfx4w',
                     ' Biography , Drama','2.30')
ninnukori=media.Movie('Ninnu Kori','Official Trailer',
                      'https://c.saavncdn.com/657/Adiga-Adiga-From-Ninnu-Kori--Telugu-2017-500x500.jpg',
                      'https://www.youtube.com/watch?v=Ia6EXfqKiV4',
                      'Comedy ,Romance',
                      '2.00')
aravinda=media.Movie('aravinda sametha',
                      'aravinda sameta official trailer',
                      'https://175732-509225-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2018/10/Aravinda-Sametha-Trailer.jpg',
                      'https://www.youtube.com/watch?v=dNMe5oRfsCE&t=16s',
                      'Action ,Entertainer',
                      '2.10')
xmen=media.Movie('x-men','x-men:dark phonex trailer',
                 'https://i.ytimg.com/vi/4MzAJpcLJoo/maxresdefault.jpg',
                 'https://www.youtube.com/watch?v=QWbMckU3AOQ&t=1s',
                 'Sci-Fi , Adventure',
                 '2.10')
avengers=media.Movie('Avengers Endgame','Official trailer HD',
                      'https://cdn1-www.superherohype.com/assets/uploads/2018/12/avengers-endgame-logo.jpg',
                      'https://www.youtube.com/watch?v=hA6hldpSTF8',
                      'Action, Adventure, Fantasy',
                      '2.48')
kgf=media.Movie('KGF Chapter 1','Official trailer',
                      'https://m.media-amazon.com/images/M/MV5BNDIwMDYxY2UtM2NhYy00NzkwLThhNDYtY2IxZGZhNjYyNmM2XkEyXkFqcGdeQXVyNDY5MTUyNjU@._V1_QL50_SY1000_CR0,0,743,1000_AL_.jpg',
                      'https://www.youtube.com/watch?v=-KfsY-qwBS0',
                      'Action, Drama ',
                      '2.48')
padipadi=media.Movie('Padi Padi Leche Manasu','Official trailer',
                      'https://m.media-amazon.com/images/M/MV5BZjAzYTkxMDQtMGFhZS00NzRjLTk1MmQtMzM0YjUyZDA5NTQ1XkEyXkFqcGdeQXVyNjY1MzUzNTQ@._V1_SY1000_CR0,0,714,1000_AL_.jpg',
                      'https://www.youtube.com/watch?v=IkLz6dhHmOQ',
                      ' Drama, Romance ',
                      '1.56')
rangasthalam=media.Movie('Rangasthalam','Official trailer',
                      'https://m.media-amazon.com/images/M/MV5BMjQ1MjFkN2EtOTU4NS00NDkzLThhNzItODkzYWNjZDMxZjE0XkEyXkFqcGdeQXVyNTgxODY5ODI@._V1_UY268_CR3,0,182,268_AL__QL50.jpg',
                      'https://www.youtube.com/watch?v=sueMmTm-M4Y',
                      ' Action, Drama ',
                      '3.00')
spiderman=media.Movie('Spiderman into the spider verse','Offiacial trailer',
                      'https://i.ytimg.com/vi/yrnPdJsMg2c/maxresdefault.jpg',
                      'https://www.youtube.com/watch?v=tg52up16eq0&t=3s',
                      'Action, Adventure, Fantasy',
                      '2.43')
goodachari=media.Movie('Goodachari','Official trailer 4K',
                      'https://m.media-amazon.com/images/M/MV5BOWQwNWRlNmUtY2FkZC00YmQ3LTlkNzUtOTUyZmExMDNkYjE2XkEyXkFqcGdeQXVyNTgxODY5ODI@._V1_QL50_SY1000_CR0,0,660,1000_AL_.jpg',
                      'https://www.youtube.com/watch?v=V-8GGhn0oDk',
                      'Action, Thriller',
                      '2.08')
uri=media.Movie('URI: The Surgical Strike','Official trailer HD',
                      'https://m.media-amazon.com/images/M/MV5BZDUxZWRiNDAtM2M4Yi00OTY4LTgyNmMtNTIzOGMwNTFiYjg0XkEyXkFqcGdeQXVyNjE1OTQ0NjA@._V1_QL50_SY1000_CR0,0,628,1000_AL_.jpg',
                      'https://www.youtube.com/watch?v=iWJ4wWefVsQ',
                      'Action',
                      '2.24')
zero=media.Movie('Zero','Official trailer HD',
                      'https://m.media-amazon.com/images/M/MV5BNzg5YjA4ZTgtZGI3MC00ODVkLTliYmEtOWQ1NTY1ODg0ZjU1XkEyXkFqcGdeQXVyNzI5NjYzODI@._V1_QL50_.jpg',
                      'https://www.youtube.com/watch?v=Ru4lEmhHTF4',
                      'Comedy, Drama, Romance',
                      '3.08')

storks=media.Movie('storkes','storkes animated movie trailer',
                    'https://upload.wikimedia.org/wikipedia/en/1/13/Storks_%28film%29_poster_2.jpg',
                    'https://www.youtube.com/watch?v=ZVzL94jZNdU',
                   'Animation , Action , Adventure','1.00')
movies=[infinity,xmen,spiderman,storks,avengers,kgf,uri,zero,aravinda,ninnukori,padipadi,goodachari]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)


