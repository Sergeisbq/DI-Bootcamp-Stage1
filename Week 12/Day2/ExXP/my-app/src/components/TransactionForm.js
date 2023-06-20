import React from 'react';
import { connect } from 'react-redux'
import { insert_transaction } from '../redux/actions';
import { useState } from 'react';

const TransactionForm = (props) => {
  const [infotransaction, setTransaction] = useState(
    {
      accountNumber: '',
      FSC: '',
      name: '',
      amount: '',
    }
  )

  const handleSubmit = (e) => {
    e.preventDefault();
    const from = e.target;
    const formData = new FormData(from);
    const all_data = Object.fromEntries(formData.entries())
    console.log("all_data", all_data);
    setTransaction(all_data);
    props.insert_data(all_data); //dispatch the action
  }

  const handleChange = (e) => {
    e.preventDefault();
    const { name, value } = e.target;
    setTransaction((prevState) => ({
    ...prevState,
    [name]: value
  }));
    
  }

  return (
    <>
    <h1>Financial Transactions:</h1>
    <form onSubmit={handleSubmit}>
    <div>
        <label htmlFor="accountNumber">Account Number:</label>
        <input
        type="text"
        name="accountNumber"
        placeholder="Enter Account Number"
        value={infotransaction.accountNumber}
        onChange={handleChange}
        />
    </div>
    <div>
        <label htmlFor="FSC">FSC:</label>
        <input
        type="text"
        name="FSC"
        placeholder="Enter FSC"
        value={infotransaction.FSC}
        onChange={handleChange}
        />
    </div>
    <div>
        <label htmlFor="accountHolderName">A/C Holder Name:</label>
        <input
        type="text"
        name="name"
        placeholder="Enter A/C Holder Name"
        value={infotransaction.name}
        onChange={handleChange}
        />
    </div>
    <div>
        <label htmlFor="amount">Amount:</label>
        <input
        type="text"
        name="amount"
        placeholder="Enter Amount"
        value={infotransaction.amount}
        onChange={handleChange}
        />
    </div>
    <button type="submit">Submit</button>
    </form>
</>
)
}

const mapDispatchToProps = (dispatch) => {
  
  return {
    insert_data: (new_transaction) => dispatch(insert_transaction(new_transaction))
  }
}

export default connect(null, mapDispatchToProps)(TransactionForm);