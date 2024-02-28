
import { CardTypes, sizes } from "./types"

import './styles.css'

const Card = ({ src, alt, title, text, link, className = '', translateX=0, translateY=0, size, ...rest }: CardTypes) => {
    className = `absolute left-0 top-0 w-[236px] p-2 ${className}`


    return (
        <a {...rest} className={className} href={link} style={{transform:`translate(${translateX}px, ${translateY}px)`}} >
            <div className="flex flex-col items-center">
                <img src={src} alt={alt} className={`${sizes[size]} w-[236px] max-w-[236px]  rounded-2xl `} />
                <div className="w-full  overflow-hidden break-words  p-1 text-left ">
                    <h3 className="line-clamp-2 font-semibold tracking-tight first-letter:capitalize">{title}</h3>
                    <p className="line-clamp-2 tracking-tighter first-letter:capitalize">{text}</p>
                </div>
            </div>
        </a>
    )
}

export default Card