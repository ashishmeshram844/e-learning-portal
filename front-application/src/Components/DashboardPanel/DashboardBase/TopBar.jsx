import React, { Fragment } from 'react'
import styles from './DashboardBase.module.css'
import ideatronLogo from '../../../assets/Image/ideatron.svg'
import ProfileIcon from '../../../assets/Image/profile.jpg'
const TopBar = ({handleToggle}) => {
  return (
    <Fragment>
        <div className={styles.TopMain}>
          <div className={styles.TopLeft}>
            <button data-td-content="Main Menu" onClick={handleToggle} type='button' className={styles.TogglButton}>
              <i className='icon-menu'></i>
            </button>
            <span title='Ideatron' className={styles.TopBarLogo}>
              <img src={ideatronLogo} alt='Ideatron'/>
            </span>
          </div>
          <div className={styles.TopMedium}>
          </div>
          <div className={styles.TopRight}>
            <div className={styles.NotificationArea}>
              <button data-td-content="Notifications" type='button' className={styles.NotiIcon}>
                <i className='icon-notifications_unread'></i>
              </button>
              <button data-td-content="Fullscreen" type='button' className={styles.NotiIcon}>
                <i className='icon-fullscreensvg'></i>
              </button>
              <button data-td-content="Settings" type='button' className={styles.NotiIcon}>
                <i className='icon-settings'></i>
              </button>
            </div>
            <div className={styles.ProfileImage}>
              <button type='button' className={styles.ProfileIcon}>
                <img src={ProfileIcon} className='w-8 h-8 rounded-full' alt='UserName'/>
              </button>
            </div>
          </div>
        </div>
    </Fragment>
  )
}

export default TopBar