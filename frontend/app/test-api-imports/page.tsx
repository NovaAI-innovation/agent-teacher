/**
 * Test page to verify API client imports work correctly.
 * This is a temporary test file - can be removed after verification.
 */

'use client';

import { useEffect, useState } from 'react';
import { apiClient, API_ENDPOINTS } from '@/lib/api';
import { wsClient } from '@/lib/websocket';

export default function TestApiImportsPage() {
  const [apiStatus, setApiStatus] = useState<string>('Checking...');
  const [wsStatus, setWsStatus] = useState<string>('Checking...');

  useEffect(() => {
    // Test API client import
    try {
      const baseURL = apiClient.defaults.baseURL;
      setApiStatus(`✅ API Client loaded. Base URL: ${baseURL}`);
    } catch (error) {
      setApiStatus(`❌ API Client error: ${error}`);
    }

    // Test WebSocket client import
    try {
      const wsState = wsClient.getState();
      const stateText =
        wsState === WebSocket.OPEN
          ? 'Connected'
          : wsState === WebSocket.CONNECTING
            ? 'Connecting'
            : wsState === WebSocket.CLOSING
              ? 'Closing'
              : wsState === WebSocket.CLOSED
                ? 'Closed'
                : 'Unknown';
      setWsStatus(`✅ WebSocket Client loaded. State: ${stateText}`);
    } catch (error) {
      setWsStatus(`❌ WebSocket Client error: ${error}`);
    }
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">API Client Import Test</h1>
      <div className="space-y-4">
        <div>
          <h2 className="text-xl font-semibold mb-2">API Client</h2>
          <p>{apiStatus}</p>
          <p className="text-sm text-gray-600 mt-2">
            Endpoints available: {Object.keys(API_ENDPOINTS).length} categories
          </p>
        </div>
        <div>
          <h2 className="text-xl font-semibold mb-2">WebSocket Client</h2>
          <p>{wsStatus}</p>
        </div>
        <div className="mt-8">
          <p className="text-sm text-gray-500">
            This is a test page. You can delete it after verifying imports work.
          </p>
        </div>
      </div>
    </div>
  );
}
