import React, { Fragment } from 'react'
import styles from './DashboardBase.module.css'
import SideMeu from './SideBarMenu.json'
import { Link } from 'react-router-dom'
const SideBar = ({sideToggle}) => {
  return (
    <Fragment>
      <div className={styles.SBBMenu}>
        {SideMeu.map((Menu, index)=> (
          (sideToggle ? 
            <Link data-tr-content={Menu.name} key={index} to={Menu.link} className={styles.SideItemBig}>
              <span className={styles.SIBIcon}><i className={Menu.icon}></i></span>
              <span className={styles.SIBTitle}>{Menu.name}</span>
            </Link>
            : 
            <Link data-tr-content={Menu.name} key={index} to={Menu.link} className={styles.SideItemSmall}>
              <span className={styles.SISIcon}>
                <i className={Menu.icon}></i>
              </span>
            </Link>
          )
        ))}
      </div>
    </Fragment>
  )
}

export default SideBar