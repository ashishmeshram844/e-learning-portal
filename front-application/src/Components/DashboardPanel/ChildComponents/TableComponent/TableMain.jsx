import React, { Fragment, useState } from "react";
import styles from "./TableCompo.module.css";

export const TableMain = (props) => {
  const {children, dataRows, checkboxRequired,handleSelectOne } = props;
  return (
    <Fragment>
      <div className={`${styles.TableResponsive}`}>
        <table className={styles.TableMain}>
          <tbody className={styles.TBody}>
            {dataRows.map((rowData, index) => (
              <tr className={`${styles.TRow} group`} key={index}>
                {checkboxRequired ? <TableCompoCheck  handleSelectOne={handleSelectOne}/> : null}
                {rowData.map((elementData, index) => (
                  <td className={styles.TData} key={index}>
                    {elementData}
                  </td>
                ))}
                {children}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Fragment>
  );
};

const TableCompoCheck = ({handleSelectOne,}) => {
  return (
    <Fragment>
      <td className={`${styles.TData} w-12`}>
        <button
          onClick={(e) => handleSelectOne(e)}
          data-value="false"
          data-td-content="select"
          type="button"
          className={styles.TableCheckUncheckBtn}
        >
          <i className="icon-check_box_outline_blank"></i>
        </button>
      </td>
    </Fragment>
  );
};

export const TableHover = (props) => {
  const { Edit, Delete, AddMember } = props;
  return (
    <Fragment>
      <td className={`${styles.THover} group-hover:flex`}>
        {Edit ? (
          <button type="button" className={styles.EditIcon}>
            <i className="icon-edit"></i>
          </button>
        ) : null}
        {Delete ? (
          <button type="button" className={styles.EditIcon}>
            <i className="icon-delete"></i>
          </button>
        ) : null}
        {AddMember ? (
          <button type="button" className={styles.EditIcon}>
            <i className="icon-add"></i>
          </button>
        ) : null}
      </td>
    </Fragment>
  );
};
