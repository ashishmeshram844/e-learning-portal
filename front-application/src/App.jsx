import React, {Suspense, Fragment} from "react";
import MainRouter from "./MainRouter";
import { BrowserRouter as Router } from 'react-router-dom';
import {QueryClient, QueryClientProvider } from 'react-query';
import Loading from "./Loading";
import './assets/Style/input.css'

const queryClient = new QueryClient();

const App = ()=>{
  return(
    <Fragment>
      <Suspense fallback={<Loading />}>
        <QueryClientProvider client={queryClient}>
          <Router>
            <MainRouter />
          </Router>
        </QueryClientProvider>
      </Suspense>
    </Fragment>
  )
}

export default App