import React, { Fragment, useState } from 'react'
import { Link } from 'react-router-dom'
import styles from './WebsiteBase.module.css';

import logo from '../../../assets/Image/ideatron.svg'
import WebMenu from './WebMenu.json'


const LoginBlock = () =>{
  return (
      <div className='flex'>
        <input type='text' placeholder='Input Username' className='mx-2 placeholder-white bg-transparent text-white border-b-2' />
        <input type='text' placeholder='Input Password' className='mx-2 placeholder-white bg-transparent text-white border-b-2' />
        <button type="submit" className='bg-white px-2'>Login</button>
        <span className="max-h-9 px-4 text-2xl">
          <i className='icon-person_remove'></i>
        </span>
      </div>
  )
}



const RegisterBlock = () =>{
  return (
      <div className='flex'>
        <input type='text' placeholder='Input Email' className='mx-2 placeholder-white bg-transparent text-white border-b-2' />
        <button type="submit" className='bg-white px-2'>Send OTP</button>
        <span className="max-h-9 px-4 text-2xl">
          <i className='icon-person_remove'></i>
        </span>
      </div>
  )
}




const WebNavBar = () => {
  const [loginView,setLoginView] = useState(false)
  const [loginBtn,setLoginBtn] = useState(true)
  const [registerView,setRegisterView] = useState(false)
  const [registerBtn,setRegisterBtn] = useState(true)

  const LoginClick = () =>{
    setLoginView(true)
    setLoginBtn(false)
    setRegisterBtn(true)
    setRegisterView(false)

  }

  const RegisterClick = () =>{
    setLoginView(false)
    setRegisterBtn(false)
    setLoginBtn(true)
    setRegisterView(true)

  }
  

  return (
    <Fragment>
      <div className={styles.NavMain}>
        <div className="grid grid-cols-12 gap-x-4 px-10 py-2 items-center">
          <div className="col-span-3">
            <Link to={'/'}>
              <img src={logo} className={styles.NavLogo} title='Ideatron' alt="nav logo" />
            </Link>
          </div>
          <div className="col-span-9">
            <div className="flex justify-end items-center gap-x-20">
              <div className={styles.NavMenu}>
                {WebMenu.map((MenuItem, Index) => (
                  <Link key={Index} to={`${MenuItem.link}`}>
                    <i className={`${MenuItem.icon}`}></i>
                    <span className='text-xs'>{MenuItem.name}</span>
                  </Link>
                ))}
              </div>
              { loginView ?
                  <LoginBlock/>  
                  : '' 
              }
              { registerView ?
                  <RegisterBlock/>  
                  : '' 
              }


              <div className="flex items-center gap-x-3">
                {
                  loginBtn ?
                  <button className={styles.SignBtn} onClick={LoginClick}><i className='icon-login'></i><span>Login</span></button>
                  : ''
                }
                {
                  registerBtn ?
                  <button className={styles.SignBtn} onClick={RegisterClick}><i className='icon-person_add'></i><span>Register</span></button>
                  :""
                }
              </div>
            </div>
          </div>
        </div>
      </div>
    </Fragment>
  )
}

export default WebNavBar