
class HTTPRequestError extends Error {
  constructor (status, body = {}, message = "") {
    super(message? message : `Bad Response: ${status}`)
    this.status = status
    this.body = body
  }
}

export {
  HTTPRequestError
}
