import { useState ,useEffect} from 'react';

import axios from 'axios';
import { AuthContext } from '../core';
import React, { useContext } from 'react'

const BudgetTransactions= () => {
  const [data, setData] = useState([]);
  const {user_type}=useContext(AuthContext);

  useEffect(() => {
    console.log(user_type);
    axios.get('http://localhost:8000/'+user_type+'/alltransactions')
      .then(response => setData(response.data.data))
      .catch(error => console.log(error));
  }, []);
  return (
    <div className='dashboard'>
      {data ? (
        <div classname="dash"> 
        { data.length===0?(
        <h3>No pending Requests</h3>
        ):(
          <div>
            <div>
                  Request_id,Amount,Type,Requested By,Balance
            </div>
            <div>
            
              {data.map((item)=> ( !item.status &&
                <div>{item.id},{item.request.request_amount},{item.request.transaction_type},{item.request.user.first_name},{item.remaining_budget}</div>

              ))}
            </div>
          </div>
        )}
        </div>
      ):(
        <p>Loading...</p>
      )}
      </div>
    );
}



export default BudgetTransactions