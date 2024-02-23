import React, { Fragment } from 'react'
import styles from './Auth.module.css'
import { Link } from 'react-router-dom'
import ideatronLogo from '../../assets/Image/ideatron.svg'
import tyroneLogo from '../../assets/Image/tyrone.svg'
import netwebLogo from '../../assets/Image/netweb.svg'
const Login = () => {
  return (
    <Fragment>
      <div className={`${styles.BgBase} grid grid-cols-2`}>
        <div className='col-span-2 flex items-center justify-center'>
          <form className={styles.FormLogin} autoComplete='off'>
            <img src={ideatronLogo} className='w-40 m-auto' />
            <h1 className={styles.FormHeading}>Login</h1>
            <div className={styles.FormGroup}>
              <label className={styles.FormLabel} htmlFor='username'>Username</label>
              <div className='flex'>
                <span className={styles.FormIcon}><i className='icon-account_circle' /></span>
                <input type='text' className={styles.FormInput} id='username' name='username' placeholder='Username' autoComplete='off'/>
              </div>
            </div>

            <div className={styles.FormGroup}>
              <label className={styles.FormLabel} htmlFor="password">Password</label>
              <div className='flex'>
                <span className={styles.FormIcon}><i className='icon-fingerprint' /></span>
                <input type='password' className={styles.FormInput} id='password' name='password' placeholder='Password' autoComplete='off'/>
              </div>
            </div>

            <div className={`${styles.FormGroup} flex justify-between  items-center`}>
              <span className='text-xs flex gap-1 items-center text-gray-500 font-medium tracking-wide'>
                <input type='checkbox' id='rememberMe' name='rememberMe'/>
                <label htmlFor='rememberMe'>Remember Me</label>              
              </span>
              <Link to={"/forgot-password"} className='text-xs flex gap-1 items-center text-blue-500 font-medium tracking-wide'>
                <i className='icon-lock_reset' />
                <span className='underline'>Forgot Password?</span>
              </Link>
            </div>

            <div className={styles.FormGroup}>
              <Link to={''} typef='submit' className={styles.LoginBtn} >
                <span>Sign In</span>
                <i className='icon-login' />
              </Link>
            </div>

            <div className={styles.FormGroup}>
              <span className='text-xs flex gap-1 items-center justify-center text-gray-500 font-medium tracking-wide'>
                Don't have an account? <Link className='text-blue-500 underline' to={'/register'}>Sign Up</Link>
              </span>
            </div>
          </form>
        </div>
        <div className="col-span-2">
          <div className={`${styles.FooterAuth}`}>
            <span>Powered By </span>
            <Link target='_blank' to={'https://tyronesystems.com'}>
                <img src={tyroneLogo}  className='w-12' />
            </Link>
            <span>&</span>
            <Link target='_blank' to={'https://netwebindia.com'}>
                <img src={netwebLogo}  className='w-14' />
            </Link>
          </div>
        </div>
      </div>
    </Fragment>
  )
}

export default Login