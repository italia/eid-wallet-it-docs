const credential = await navigator.credentials.get({
  digital: {
    requests: [
      {
        protocol: "openid4vp-v1-signed",
        data: {
          request: signedRequest
        }
      }
    ]
  }
});
