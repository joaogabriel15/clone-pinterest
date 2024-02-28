import { ButtonTypes } from "./types"

enum themes{
 "bg-[#745bce] text-white hover:border-[#8d71e7]",
 "bg-white text-[#745bce] hover:border-[#8d71e7]",
 "bg-[#402f9d] text-white hover:border-[#8d71e7]",
}

const Button = ({label, theme, className = '', ...rest}:ButtonTypes) =>{
    className = `h-10 w-auto flex-none max-w-36 text-nowrap rounded-full border-2 px-9 py-1 font-bold ${themes[theme]} ${className}`

   return (
    <button  {...rest} className={className}>
        {label}
    </button>
   )
}

export default Button