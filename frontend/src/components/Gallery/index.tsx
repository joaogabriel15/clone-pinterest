import { useEffect, useState } from "react"
import Card from "./Card"
import { sizes } from "./Card/types"

// Foi colocado mais de uma vez na lista de tamanhos o medium
// para que a chance dele aparecer seja maior que os outros
// sendo 60% de chance dele aparecer.
const SizesOptions: sizes[] = [sizes.small, sizes.medium, sizes.medium, sizes.medium, sizes.high]
const generateSizeOption = () => SizesOptions[Math.floor(Math.random() * (SizesOptions.length))]





type item = {
    id: number
    height?: string
    hasText: boolean
    src: string
    title: string
    text?: string
}

const columns = [10, 260, 520, 780, 1040, 1300, 1560]



const items: item[] = [
    {
        "id": 1,
        "src": "https://randomwordgenerator.com/img/picture-generator/50e9d4414851b10ff3d8992cc12c30771037dbf85254794e732873dc954f_640.jpg",
        "title": "Cachorro Fofo",
        "hasText": false
    },
    {
        "id": 2,
        "src": "https://randomwordgenerator.com/img/picture-generator/51e9d145435bb10ff3d8992cc12c30771037dbf85254794e732a7dd09644_640.jpg",
        "title": "Cachorro Brincalhão",
        "hasText": false
    },
    {
        "id": 3,
        "src": "https://randomwordgenerator.com/img/picture-generator/51e1dd444351b10ff3d8992cc12c30771037dbf85254794e732c79d79044_640.jpg",
        "title": "Cachorro Amigável",
        "hasText": false
    },
    {
        "id": 4,
        "src": "https://randomwordgenerator.com/img/picture-generator/martino-pietropoli-6k2wkqGMw1I-unsplash.jpg",
        "title": "Cachorro Adorável",
        "hasText": false
    },
    {
        "id": 5,
        "src": "https://randomwordgenerator.com/img/picture-generator/57e2dd474f53ae14f1dc8460962e33791c3ad6e04e5074417d2e7ed6954bc7_640.jpg",
        "title": "Cachorro Divertido",
        "hasText": false
    },
    {
        "id": 6,
        "src": "https://randomwordgenerator.com/img/picture-generator/57e0d7424e57ab14f1dc8460962e33791c3ad6e04e507749712e79d3964bc4_640.jpg",
        "title": "Cachorro Divertido",
        "hasText": false
    },
    {
        "id": 7,
        "src": "https://randomwordgenerator.com/img/picture-generator/54e4d2444855a814f1dc8460962e33791c3ad6e04e507440762879dc974fcd_640.jpg",
        "title": "Cachorro Divertido",
        "hasText": false
    },
    {
        "id": 8,
        "src": "https://randomwordgenerator.com/img/picture-generator/57e2dd474f53ae14f1dc8460962e33791c3ad6e04e5074417d2e7ed6954bc7_640.jpg",
        "title": "Cachorro Divertido",
        "hasText": false
    },
    {
        "id": 9,
        "src": "https://randomwordgenerator.com/img/picture-generator/57e2dd474f53ae14f1dc8460962e33791c3ad6e04e5074417d2e7ed6954bc7_640.jpg",
        "title": "Cachorro Divertido",
        "hasText": false
    },
    {
        "id": 10,
        "src": "https://randomwordgenerator.com/img/picture-generator/57e2dd474f53ae14f1dc8460962e33791c3ad6e04e5074417d2e7ed6954bc7_640.jpg",
        "title": "Cachorro Divertido",
        "hasText": false
    }
]

const Gallery = () => {
    const [cardsCache, setCardsCache] = useState<JSX.Element[]>([])
    const [itemsCache, setItemsCache] = useState([])



    const getTranslateHeight = (itemsCache: any, localCounter: number, nivel: number) => {
        let height = 0
        
        if (localCounter > 6) {
            if (localCounter % 7 === 0 && localCounter > 6) {
                nivel++
            }

            const item = itemsCache[localCounter - 7 * nivel]

            if (sizes[item.size] == 'medium') {
                height = 375
            } else if (sizes[item.size] == 'high') {
                height = 457
            } else {
                height = 186
            }

            if (item.hasText == true) {
                height = height + 20
            }
        }

        return [height, nivel]
    }

    useEffect(() => {
        const localItems = items.map((item: item) => {
            const localItem = {
                ...item,
                size: generateSizeOption(),
            }

            return localItem
        })

        setItemsCache(localItems)

    }, [])

    
    useEffect(() => {
        let localCounter = 0
        // eslint-disable-next-line prefer-const
        let nivel = 0
        let translateY = 0

        const cards: JSX.Element[] = itemsCache.map((item) => {
            [translateY, nivel] = getTranslateHeight(itemsCache, localCounter, nivel)

            const card = (
                <Card
                    key={`card-${localCounter}`}
                    size={item.size}
                    src={item.src}
                    translateX={columns[localCounter % 7]}
                    translateY={translateY}
                    title={item.title}
                    text={item.text}
                />
            )
            console.log('nivel - ',nivel)

            localCounter++
            return card
        })

        console.log(cards)
        setCardsCache(cards)
    }, [    itemsCache])

   

    return (
        <main style={{ height: `calc(${cardsCache.length}*110px)` }} className="relative mx-12 bg-slate-400 ">
            {
              items && cardsCache
            }
        </main>
    )

}

export default Gallery