import React, { useState, Fragment, useEffect } from "react";
import styles from "./TableCompo.module.css";

const TableCompoTop = (props) => {
  const {handleSelectAll } = props
  const [toggleADSearch, setToggleADSearch] = useState()
  const handletoggleADSearch = (event) => {
    event.stopPropagation()
    setToggleADSearch((prevToggle) => !prevToggle)
    const formSet = event.currentTarget.parentElement.parentElement;
    const formSetDataValue = formSet.getAttribute('data-form')
    const newDataValue = formSetDataValue === 'true' ? 'false' : 'true'
    formSet.setAttribute('data-form', newDataValue)
  }


  return (
    <Fragment>
      <div className={styles.TableCompoTop}>
        <div className="col-span-3">
          <div className="flex justify-start">
            <SelectAll handleSelectAll={handleSelectAll} />
            <Refresh />
            <DeleteAll />
          </div>
        </div>
        <div className="col-span-6">
          <div className="flex justify-start">
            <Search handletoggleADSearch={handletoggleADSearch}>
              {toggleADSearch ? <AdvanceSearch /> : null}
            </Search>
          </div>
        </div>
        <div className="col-span-3">
          <div className="flex justify-end">
            <Pagination />
            <Short />
            <ListGrid />
          </div>
        </div>
      </div>
    </Fragment>
  );
};

const SelectAll = ({handleSelectAll }) => {
  return (
    <Fragment>
      <div className={styles.SelectAll}>
        <button
          data-attr="false"
          onClick={(e) => handleSelectAll(e)}
          data-td-content="Select All"
          type="button"
          className={styles.CheckUncheckBtn}
        >
          <i className="icon-indeterminate_check_box"></i>
        </button>
      </div>
    </Fragment>
  );
};

const Refresh = () => {
  return (
    <Fragment>
      <div className={styles.Refresh}>
        <button
          data-td-content="Refresh"
          type="button"
          className={styles.RefreshBtn}
        >
          <i className="icon-refresh"></i>
        </button>
      </div>
    </Fragment>
  );
};

const DeleteAll = () => {
  return (
    <Fragment>
      <div className={styles.DeleteAll}>
        <button
          data-td-content="Delete All"
          type="button"
          className={styles.DeleteAllBtn}
        >
          <i className="icon-delete"></i>
          {/* <i className="icon-delete_forever"></i> */}
        </button>
      </div>
    </Fragment>
  );
};

const Search = ({children, handletoggleADSearch}) => {
  return (
    <Fragment>
      <fieldset className={styles.SearchMain} data-form="true">
        <form className={styles.SearchArea} >
          <button data-td-content="Search" type="submit" className={styles.SIcon}>
            <i className="icon-search"></i>
          </button>
          <input type="text" className={styles.SInput} placeholder="Search" />
          {/* <button type='reset'  data-td-content="Reset" className={styles.RIcon}><i className='icon-close'></i></button> */}
          <button
            type="button"
            data-td-content="Search options"
            className={styles.ASIcon}
            onClick={(event) => handletoggleADSearch(event)}
          >
            <i className="icon-tune"></i>
          </button>
        </form>
        {children}
      </fieldset>
    </Fragment>
  );
};

const Pagination = () => {
  return (
    <Fragment>
      <div className={styles.PaginationMain}>
        <button type="button" className={styles.PaginationShow}>
          <span>1-100</span>
          <span>of</span>
          <span>816</span>
        </button>
        <div className={styles.PrevNext}>
          <button
            data-td-content="Prev"
            type="button"
            className={styles.PrevBtn}
          >
            <i className="icon-keyboard_arrow_left"></i>
          </button>
          <button
            data-td-content="Next"
            type="button"
            className={styles.NextBtn}
          >
            <i className="icon-keyboard_arrow_right"></i>
          </button>
        </div>
      </div>
    </Fragment>
  );
};

const Short = () => {
  return (
    <Fragment>
      <div data-td-content="Sort" className={styles.ShortMain}>
        <button className={styles.AscendingBtn} type="button">
          <i className="icon-arrow_drop_up"></i>
        </button>
        <span className={styles.AtoZ}>AZ</span>
        <button className={styles.DescendingBtn} type="button">
          <i className="icon-arrow_drop_down"></i>
        </button>
      </div>
    </Fragment>
  );
};

const ListGrid = () => {
  return (
    <Fragment>
      <div className={styles.ListGrid}>
        <button data-td-content="List View" className={styles.ListGridBtn}>
          <i className="icon-view_list"></i>
          {/* <i className="icon-view_module"></i> */}
        </button>
      </div>
    </Fragment>
  );
};

const AdvanceSearch = () => {
  return (
    <Fragment>
      <div className={styles.AdvanceSearch}>
        <div className={styles.ADSFormTab}>
          sajan
        </div>
        <form className={styles.ADSForm}>
          sajan
        </form>
      </div>
    </Fragment>
  );
};

export default TableCompoTop;
