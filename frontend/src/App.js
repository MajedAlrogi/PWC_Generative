import React from 'react';
import ChatbotUI from './components/ChatbotUI.js';
import { WebSocketProvider } from './services/websocket.js';
import './App.css';

const App = () => {
	return (
		<WebSocketProvider>
			<div className='App'>
				<header className='App-header'>
					<ChatbotUI />
				</header>
			</div>
		</WebSocketProvider>
	);
};

export default App;
