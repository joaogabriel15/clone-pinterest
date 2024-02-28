
export enum sizes {
    'small', 'medium', 'high'
}

export type CardTypes = React.ComponentPropsWithRef<'a'> & {
    src: string
    alt?: string
    title: string
    text?: string
    link?: string
    size: sizes
    translateX?: number
    translateY?: number
    pato: (h:number)=> void 
}