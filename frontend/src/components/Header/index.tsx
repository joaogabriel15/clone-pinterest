import Logo from '../../assets/PinterestLogo.png'
import Button from '../Button'

const Header = () => {
    return (
        <header className=" mx-6 my-3 flex  flex-row items-center  gap-5 ">
            <div className='flex w-1/12 flex-none  flex-row items-center justify-center'>
            <img src={Logo} className='size-14'/>
            <h1 className='  text-2xl   font-bold'>Pinterest</h1>
            </div>
           
           <form className='flex w-8/12 flex-none  grow flex-row items-center justify-center gap-1 '>
            <input className=' h-12 w-full  rounded-full border-2 bg-[#342c32]/[0.1] pl-3 hover:border-[#8d71e7] focus:border-[#8d71e7] focus:outline-0 '></input>
            <Button label="Search" theme={0}/>
           </form>

           <div className='flex w-2/12 flex-none  items-center justify-end gap-1 '>
           <Button  label="Sign up" theme={1}/>
           <Button  label="Log in" theme={2}/>
           </div>
        </header>
    )
  }
  
  export default Header
  