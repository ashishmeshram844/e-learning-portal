import React, { Fragment, useState } from "react";
import styles from "./DashboardBase.module.css";
import { Routes, Route } from "react-router-dom";

import TopBar from './TopBar'
import SideBar from './SideBar'
import DashbaordMain from "../DashboardMain/DashboardMain";
import BottomBar from "./BottomBar";

const DashboardBase = () => {
  const [sideToggle, setSideToggle ] = useState()
  const handleToggle = () => {
    setSideToggle((prevSize) => !prevSize);
  };
  return (
    <Fragment>
      <div className={styles.DMain}>
        <TopBar handleToggle={handleToggle}/>
        <div className={`${styles.SideMain} ${sideToggle ? 'w-[15rem]' : 'w-[4.5rem]'}`}>
          <SideBar sideToggle={sideToggle} />
        </div>
        <div className={`${styles.MainBar} ${sideToggle ? "ml-[15rem]" : "ml-[4.5rem]"}`}>
          <Routes>
            <Route path={'*'} element={<DashbaordMain />} />
          </Routes>
        </div>
        <BottomBar/>
      </div>
    </Fragment>
  );
};

export default DashboardBase;
