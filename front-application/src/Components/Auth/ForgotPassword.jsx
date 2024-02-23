import React, { Fragment } from "react"
import styles from "./Auth.module.css"
import { Link } from "react-router-dom"
import ideatronLogo from "../../assets/Image/ideatron.svg"
import tyroneLogo from '../../assets/Image/tyrone.svg'
import netwebLogo from '../../assets/Image/netweb.svg'
const ForgotPassword = () => {
  return (
    <Fragment>
      <div className={`${styles.BgBase} grid grid-cols-2`}>
        <div className="col-span-2 flex items-center justify-center">
          <form className={styles.FormRegister} autoComplete="off">
            <img src={ideatronLogo} className="w-40 m-auto" />
            <h1 className={styles.FormHeading}>Forgot Password</h1>
            <div className="grid grid-cols-2 gap-x-2">
              <div className={`${styles.FormGroup} col-span-1`}>
                <label className={styles.FormLabel} htmlFor="username">
                  Username
                </label>
                <div className="flex">
                  <span className={styles.FormIcon}>
                    <i className="icon-account_circle" />
                  </span>
                  <input
                    type="text"
                    className={styles.FormInput}
                    id="username"
                    name="username"
                    placeholder="Username"
                    autoComplete="off"
                    required
                  />
                </div>
              </div>
              <div className={`${styles.FormGroup} col-span-1`}>
                <label className={styles.FormLabel} htmlFor="username">
                  Email
                </label>
                <div className="flex">
                  <span className={styles.FormIcon}>
                    <i className="icon-alternate_email" />
                  </span>
                  <input
                    type="email"
                    className={styles.FormInput}
                    id="username"
                    name="username"
                    placeholder="Email Id"
                    autoComplete="off"
                    required
                  />
                </div>
              </div>
            </div>
            <div className="grid grid-cols-2 gap-x-2">
              <div className={`${styles.FormGroup} col-span-1`}>
                <label className={styles.FormLabel} htmlFor="username">
                  Password
                </label>
                <div className="flex">
                  <span className={styles.FormIcon}>
                    <i className="icon-key" />
                  </span>
                  <input
                    type="text"
                    className={styles.FormInput}
                    id="username"
                    name="username"
                    placeholder="Password"
                    autoComplete="off"
                    required
                  />
                </div>
              </div>
              <div className={`${styles.FormGroup} col-span-1`}>
                <label className={styles.FormLabel} htmlFor="username">
                  Confirm Password
                </label>
                <div className="flex">
                  <span className={styles.FormIcon}>
                    <i className="icon-fingerprint" />
                  </span>
                  <input
                    type="text"
                    className={styles.FormInput}
                    id="username"
                    name="username"
                    placeholder="Confirm Password"
                    autoComplete="off"
                    required
                  />
                </div>
              </div>
            </div>
            <div className={styles.FormGroup}>
              <button typef="submit" className={styles.LoginBtn}>
                <span>Forgot Password</span>
                <i className="icon-lock_reset" />
              </button>
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
  );
};

export default ForgotPassword;
