import React, { Fragment } from 'react'
import styles from './Auth.module.css'
import { Link } from 'react-router-dom'
import ideatronLogo from '../../assets/Image/ideatron.svg'
const Register = () => {
  return (
    <Fragment>
      <div className={`${styles.BgBase} grid grid-cols-2`}>
        <div className='col-span-2 flex items-center justify-center'>
          <form className={styles.FormRegister} autoComplete='off'>
            <img src={ideatronLogo} className='w-40 m-auto' alt="logo" />
            <h1 className={styles.FormHeading}>Register</h1>
            <div className="grid grid-cols-2 gap-x-2">
              <div className={`${styles.FormGroup} col-span-1`}>
                <label className={styles.FormLabel} htmlFor='username'>Username</label>
                <div className='flex'>
                  <span className={styles.FormIcon}><i className='icon-account_circle' /></span>
                  <input type='text' className={styles.FormInput} id='username' name='username' placeholder='Username' autoComplete='off' required/>
                </div>
              </div>
              <div className={`${styles.FormGroup} col-span-1`}>
                <label className={styles.FormLabel} htmlFor='username'>Full Name</label>
                <div className='flex'>
                  <span className={styles.FormIcon}><i className='icon-person' /></span>
                  <input type='text' className={styles.FormInput} id='username' name='username' placeholder='Full Name' autoComplete='off' required/>
                </div>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-x-2">
              <div className={`${styles.FormGroup} col-span-1`}>
                <label className={styles.FormLabel} htmlFor='username'>Email</label>
                <div className='flex'>
                  <span className={styles.FormIcon}><i className='icon-alternate_email' /></span>
                  <input type='email' className={styles.FormInput} id='username' name='username' placeholder='Email Id' autoComplete='off' required/>
                </div>
              </div>
              <div className={`${styles.FormGroup} col-span-1`}>
                <label className={styles.FormLabel} htmlFor='username'>Mobile Number</label>
                <div className='flex'>
                  <span className={styles.FormIcon}><i className='icon-smartphone' /></span>
                  <input type='text' className={styles.FormInput} id='username' name='username' placeholder='Mobile Number' autoComplete='off' required/>
                </div>
              </div>
            </div>
            <div className="grid grid-cols-2 gap-x-2">
              <div className={styles.FormGroup}>
                <label className={styles.FormLabel} htmlFor="password">Password</label>
                <div className='flex'>
                  <span className={styles.FormIcon}><i className='icon-key' /></span>
                  <input type='password' className={styles.FormInput} id='password' name='password' placeholder='Password' autoComplete='off'/>
                </div>
              </div>
              <div className={styles.FormGroup}>
                <label className={styles.FormLabel} htmlFor="password">Confirm Password</label>
                <div className='flex'>
                  <span className={styles.FormIcon}><i className='icon-fingerprint' /></span>
                  <input type='password' className={styles.FormInput} id='password' name='password' placeholder='Confirm Password' autoComplete='off'/>
                </div>
              </div>
            </div>


            <div className={styles.FormGroup}>
              <button typef='submit' className={styles.LoginBtn} >
                <span>Sign Up</span>
                <i className='icon-person_add' />
              </button>
            </div>

            <div className={styles.FormGroup}>
              <span className='text-xs flex gap-1 items-center justify-center text-gray-500 font-medium tracking-wide'>
                Already have an account? <Link className='text-blue-500 underline' to={'/login'}>Sign In</Link>
              </span>
            </div>
          </form>
        </div>
        

      </div>
    </Fragment>
  )
}

export default Register