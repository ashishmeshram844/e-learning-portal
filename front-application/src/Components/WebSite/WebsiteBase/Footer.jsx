import React, { Fragment } from 'react'
import tyroneLogo from '../../../assets/Image/tyrone.svg'
import netwebLogo from '../../../assets/Image/netweb.svg'
import styles from './WebsiteBase.module.css'
import { Link } from 'react-router-dom'
const Footer = () => {
  return (
    <Fragment>
        <div className={`${styles.FooterMain}`}>
          <span>Powered By </span>
          <Link target='_blank' to={'https://tyronesystems.com'}>
              <img src={tyroneLogo}  className='w-12' />
          </Link>
          <span>&</span>
          <Link target='_blank' to={'https://netwebindia.com'}>
              <img src={netwebLogo}  className='w-14' />
          </Link>
        </div>
    </Fragment>
  )
}

export default Footer