import React, { Fragment } from 'react'
import { Link } from 'react-router-dom'
import styles from './WebsiteBase.module.css';

import logo from '../../../assets/Image/ideatron.svg'
import WebMenu from './WebMenu.json'

const WebNavBar = () => {
  return (
    <Fragment>
      <div className={styles.NavMain}>
        <div className="grid grid-cols-12 gap-x-4 px-10 py-2 items-center">
          <div className="col-span-3">
            <Link to={'/'}>
              <img src={logo} className={styles.NavLogo} title='Ideatron' />
            </Link>
          </div>
          <div className="col-span-9">
            <div className="flex justify-end items-center gap-x-6">
              <div className={styles.NavMenu}>
                {WebMenu.map((MenuItem, Index) => (
                  <Link key={Index} to={`${MenuItem.link}`}>
                    <i className={`${MenuItem.icon}`}></i>
                    <span className='text-xs'>{MenuItem.name}</span>
                  </Link>
                ))}
              </div>
              <div className={styles.SignBtn}>
                <Link to={'/login'}>
                  <i className='icon-login'></i>
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Fragment>
  )
}

export default WebNavBar