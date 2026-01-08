/**
 * Test page to verify environment variables are accessible.
 * This is a temporary test file - can be removed after verification.
 */

'use client';

import { useEffect, useState } from 'react';

export default function TestEnvPage() {
  const [envStatus, setEnvStatus] = useState<string>('Checking...');

  useEffect(() => {
    // Test environment variable access
    const apiUrl = process.env.NEXT_PUBLIC_API_URL;

    if (apiUrl) {
      setEnvStatus(`✅ Environment variable accessible: ${apiUrl}`);
    } else {
      setEnvStatus('❌ Environment variable not accessible');
    }
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Environment Variable Test</h1>
      <div className="space-y-4">
        <div>
          <h2 className="text-xl font-semibold mb-2">NEXT_PUBLIC_API_URL</h2>
          <p>{envStatus}</p>
          <p className="text-sm text-gray-600 mt-2">
            Value: {process.env.NEXT_PUBLIC_API_URL || 'Not set'}
          </p>
        </div>
        <div className="mt-8">
          <p className="text-sm text-gray-500">
            This is a test page. You can delete it after verifying environment variables work.
          </p>
        </div>
      </div>
    </div>
  );
}
